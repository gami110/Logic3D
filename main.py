import pandas as pd
from fastapi import File
# from api import Container

# Функция для работы с файлом
def calculation_single_cargo_in_container(name, length, width, height, weight, count, rotation, stacking, combination, Hcont, Wcont, Lcont, Qcont, min_price, over_price):
    n = count
    Ncont = 0
    vgr = (height * width * length) / 10 ** 9
    Vcont = (Hcont * Wcont * Lcont) / 10 ** 9
    # Сколько влезит коробок по массе
    count_weight = Qcont // weight
    # Сколько влезит по объему

    if stacking == 1:
        h1 = Hcont // height
    else:
        h1 = 1
    # h1 = Hcont // height
    b1 = Wcont // width
    l1 = Lcont // length
    g_all = h1 * b1 * l1
    if rotation == 1:
        b_ost = Wcont - (b1 * width)  # место по ширине
        l_ost = Lcont - (l1 * length)  # место по длине
        if b_ost >= width:
            h_1 = Hcont // height
            b_1 = b_ost // width
            l_1 = Lcont // length
            g_all += h_1 * b_1 * l_1
        elif b_ost >= length:
            h_1 = Hcont // height
            b_1 = b_ost // length
            l_1 = Lcont // width
            g_all += h_1 * b_1 * l_1
        elif l_ost >= length:
            h_1 = Hcont // height
            b_1 = Wcont // width
            l_1 = l_ost // length
            g_all += h_1 * b_1 * l_1
        elif l_ost >= width:
            h_1 = Hcont // height
            b_1 = Wcont // length
            l_1 = l_ost // width
            n_n = h_1 * b_1 * l_1
            if n_n + g_all < count_weight:
                g_all += n_n
            else:
                g_all += count_weight - g_all
    if count_weight <= g_all:
        while n >= 0:
            Ncont += 1
            n = n - count_weight
            g_all = count_weight
    else:
        while n >= 0:
            Ncont += 1
            n = n - g_all
    if (g_all*weight/1000) > 10:
        price_cont = min_price + (over_price * (g_all * weight / 1000) - 10)
    else:
        price_cont = min_price
    sum_price = price_cont*Ncont

    return {
        'Наименования груза': name,
        'Колличество груза, шт': count,
        'Количество груза в одном контейнереб, шт': g_all,
        'Объем груза в одном контейнере, м3': g_all * vgr,
        'Масса груза в одном контейнере, т': g_all * weight / 1000,
        'Общая масса груза, т': count * weight / 1000,
        'Количество контейнеров, шт': Ncont,
        'Стоимость погрузки одного контейнера, руб': price_cont,
        'Стоимость погрузки всех контейнеров, руб': sum_price
    }

    # print(
    #     f"Наименования груза: {name};",
    #     f"Количество контейнеров: {Ncont} шт;",
    #     f"Количество груза в одном контейнере: {g_all} шт;",
    #     f"Объем груза в одном контейнере: {g_all * vgr}/{Vcont} м3,",
    #     f"Масса груза в одном контейнере: {g_all * weight / 1000}/{Qcont / 1000} тонн;",
    # ),
    # data1['Наименования груза'].append(name)
    # data1['Количество контейнеров'].append(Ncont)
    # data1['Количество груза в одном контейнере'].append(g_all)
    # data1['Объем груза в одном контейнере'].append(g_all * vgr)
    # data1['Масса груза в одном контейнере'].append(g_all * weight/1000)
    # data1['Колличество груза'].append(count)
    # data1['Общая масса груза'].append(count*weight/1000)


def calc(container, cargo_params_file: File = None, cargo_params_file_path: str = None, cargo_params_raw = None):
    cargo_params = pd.read_excel(cargo_params_file_path if cargo_params_file_path else cargo_params_file, index_col=0)
    print(container)
    # name, length, width, height, weight, count, rotation, stacking, combination = row
    Hcont, Wcont, Lcont, Qcont, min_price, over_price = container['height'], container['width'], container['length'], container['weight'], 5000, 600
    result = [calculation_single_cargo_in_container(*row, Hcont, Wcont, Lcont, Qcont, min_price, over_price) for row in cargo_params.itertuples()]
    filename = 'result.xlsx'
    pd.DataFrame(result).to_excel(filename, index=False)
    return filename


if __name__ == '__main__':
    pass
    # # data1 = {'Наименования груза': [],
    # #          'Колличество груза': [],
    # #          'Общая масса груза': [],
    # #          'Количество контейнеров': [],
    # #          'Количество груза в одном контейнере': [],
    # #          'Объем груза в одном контейнере': [],
    # #          'Масса груза в одном контейнере': [],
    # #
    # #          }
    # results = calc({'height': 2500, 'width': 2000, 'length': 7000, 'weight': 10000, 'pricemin': 5000, 'priceone': 500}, cargo_params_file_path='data.xlsx')
    # pd.DataFrame(results).to_excel('result2.xlsx', index=False)
