import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from pydantic import BaseModel
import uuid
from main import calc

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class Container(BaseModel):
    length: int
    width: int
    height: int
    weight: int
    # pricemin: int


class Cargo(BaseModel):
    length: int
    width: int
    height: int
    weight: int


@app.get("/api/test")
async def test():
    print("test")
    return "Test"


files: dict[str, bytes] = {}
@app.post("/api/sendFile")
async def send_file(file: bytes = File(default=None)):
    file_uuid = str(uuid.uuid1())
    files[file_uuid] = file
    return file_uuid

@app.post("/api/calcCargoParamsFile")
async def get_cargo_params_file(request: dict):#file_id: str, container_type: Container):
    filename = calc(request['container'], cargo_params_file=files[request['id']])
    headers = {'Content-Disposition': 'attachment; filename="result.xlsx"'}
    return FileResponse(path=filename, headers=headers)


@app.post("/api/calcCargoParamsRaw")
async def get_cargo_params_raw(cargo_params: list[Cargo], container_type: Container):
    pass
    # return calc(container_type, cargo_params_raw=cargo_params)


# @app.post("/api/containerParams")
# async def get_container_params(container_type: Container):
#     return container[container_type.name]


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=60740)