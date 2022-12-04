import pandas as pd

# import math

df = pd.read_excel('data.xlsx')
#Функция для работы с файлом
def some_func(df):
    for row in df.itertuples():
        name = row[1]
        length = row[2]
        width = row[3]
        height = row[4]
        weight = row[5]
        count = row[6]

        return name, length, width, height, weight, count

name, length, width, height, weight, count = some_func(df)
Hcont, Wcont, Lcont, Qcont = 2390, 2350, 5900, 21700

result = {"Наименования груза": "name",
          "Количество контейнеров": "5",
          "Количество груза в одном контейнере": "",}
def var1():
    n = count
    Ncont = 0
    vgr = (height * width * length)/10**9
    Vcont = (Hcont * Wcont * Lcont)/10**9
    # Сколько влезит коробок по массе
    count_weight = Qcont//weight
    # print(count_weight)
    # Сколько влезит по объему
    h1 = Hcont // height
    b1 = Wcont // width
    l1 = Lcont // length
    g_all = h1 * b1 * l1
    # print(g_all)
    b_ost = Wcont - (b1 * width)  # место по ширине
    l_ost = Lcont - (l1 * length)  # место по длине
    # print(b_ost, l_ost)
    if b_ost >= width:
        h_1 = Hcont // height
        b_1 = b_ost // width
        l_1 = Lcont // length
        g_all += h_1 * b_1 * l_1
        # print(1)
    elif b_ost >= length:
        h_1 = Hcont // height
        b_1 = b_ost // length
        l_1 = Lcont // width
        g_all += h_1 * b_1 * l_1
        # print(2)
    elif l_ost >= length:
        h_1 = Hcont // height
        b_1 = Wcont // width
        l_1 = l_ost // length
        g_all += h_1 * b_1 * l_1
        # print(3)
    elif l_ost >= width:
        h_1 = Hcont // height
        b_1 = Wcont // length
        l_1 = l_ost // width
        n_n = h_1 * b_1 * l_1
        # print(n_n)
        if n_n+g_all < count_weight:
            g_all += n_n
        else:
            g_all += count_weight-g_all
    #     print(4)
    # else:
    #     print(g_all)

    if count_weight <= g_all:
        while n >= 0:
            Ncont += 1
            n = n-count_weight
            g_all = count_weight
    else:
        while n >= 0:
            Ncont += 1
            n = n - g_all

    print(
        f"Наименования груза: {name};",
        f"Количество контейнеров: {Ncont} шт;",
        f"Количество груза в одном контейнере: {g_all} шт;",
        f"Объем груза в одном контейнере: {g_all*vgr}/{Vcont} м3,",
        f"Масса груза в одном контейнере: {g_all*weight/ 1000}/{Qcont / 1000} тонн;",
        ),






var1()

# result["Наименования груза"] = str(name)
#     result["Количество контейнеров"] = str(Ncont)
#     result["Количество груза в одном контейнере"] = str(g_all)
#     result["Объем груза в одном контейнере"] = str(g_all*vgr)
#     result["Масса груза в одном контейнере"] = str(g_all*weight/ 1000)
#     df1 = pd.DataFrame([result])
#     df1.to_excel('result.xlsx', index=False)
#     print(df1)
# vall = vgr * g_all
#             mall = g_all * weight
#             ncont = math.ceil(weight / g_all)
# print(
#                 f"Наименования груза: {name}",
#                 f"Колличество контейнеров: {Ncont},"
#                 f"Заполненый объем: {vall/10**9} м3,"
#                 f"Масса всего груза: {mall/1000},"
#                 f"Грузоподъемность контейнера/контейнеров: {Qcont/1000}/{Qcont/1000*ncont}, "
#                 f"Груза в одном контейнере: {g_all}")