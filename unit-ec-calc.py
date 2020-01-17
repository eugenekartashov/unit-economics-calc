import numpy as np
import pandas as pd
import time

unitec = pd.DataFrame({'User Aquisition': np.zeros(5, dtype=int),
                       'Convert to purchase': np.zeros(5, dtype=float),
                       'Buyers': np.zeros(5, dtype=int),
                       'iCount': np.zeros(5, dtype=float),
                       'iPrice': np.zeros(5, dtype=float),
                       'AvPrice': np.zeros(5, dtype=float),
                       'COGS, %': np.zeros(5, dtype=float),
                       'COGS, fix': np.zeros(5, dtype=float),
                       '1stCOGS': np.zeros(5, dtype=float),
                       'COGS, total': np.zeros(5, dtype=float),
                       'AvPaymentCount': np.zeros(5, dtype=float),
                       'AvRevenue per Customer': np.zeros(5, dtype=float),
                       'AvRevenue per User': np.zeros(5, dtype=float),
                       'Cost per Acquisition': np.zeros(5, dtype=float),
                       'Marketing cost': np.zeros(5, dtype=float),
                       'Contribution Margin': np.zeros(5, dtype=float)},
                      columns=['User Aquisition', 'Convert to purchase', 'Buyers', 'iCount', 'iPrice', 'AvPrice',
                               'COGS, %', 'COGS, fix', 'COGS, total', '1stCOGS', 'AvPaymentCount',
                               'AvRevenue per Customer', 'AvRevenue per User', 'Cost per Acquisition',
                               'Marketing cost', 'Contribution Margin'])

# Счётчик строки
i = 0


def ue_input(i, f):
    if f == 0:
        while True:
            try:
                unitec.loc[i, 'User Aquisition'] = int(input("1/9. Сколько у вас пользователей?\n"))
                if unitec.loc[i, 'User Aquisition'].dtype is 'string':
                    raise ValueError
                break
            except ValueError:
                print(
                    "Это не число. Попробуйте ещё раз!")
    elif f == 1:
        while True:
            try:
                unitec.loc[i, 'Convert to purchase'] = float(input("2/9. Какая конверсия в покупателя? "
                                                                   "Введите число от 0 до 1\n"))
                if unitec.loc[i, 'Convert to purchase'] < 0.0 or unitec.loc[i, 'Convert to purchase'] > 1.0:
                    raise Exception
                break
            except ValueError:
                print(
                    "Это не число. Попробуйте ещё раз!")
            except Exception:
                print('Число должно быть между 0 и 1')
    elif f == 2:
        while True:
            try:
                unitec.loc[i, 'iCount'] = float(input("3/9. Сколько в среднем товаров в корзине покупателя?\n"))
                if unitec.loc[i, 'iCount'].dtype is 'string':
                    raise ValueError
                break
            except ValueError:
                print(
                    "Это не число. Попробуйте ещё раз!")
    elif f == 3:
        while True:
            try:
                unitec.loc[i, 'iPrice'] = float(input("4/9. Какая средняя стоимость корзины?\n"))
                if unitec.loc[i, 'iPrice'].dtype is 'string':
                    raise ValueError
                break
            except ValueError:
                print(
                    "Это не число. Попробуйте ещё раз!")
    elif f == 4:
        while True:
            try:
                unitec.loc[i, 'COGS, %'] = float(
                    input("5/9. Какую долю от продажи вы тратите (комиссии банку, продажнику, etc.)?"
                          " Если не платите, впишите ноль\n"))
                if unitec.loc[i, 'COGS, %'] < 0.0 or unitec.loc[i, 'COGS, %'] > 1.0:
                    raise Exception
                break
            except ValueError:
                print(
                    "Это не число. Попробуйте ещё раз!")
            except Exception:
                print('Число должно быть между 0 и 1')
    elif f == 5:
        while True:
            try:
                unitec.loc[i, 'COGS, fix'] = float(
                    input("6/9. Какую фиксированную сумму от продажи вы тратите (на производство, "
                          "комиссию продажнику, etc.)? Если не платите, впишите ноль\n"))
                if unitec.loc[i, 'COGS, fix'].dtype is 'string':
                    raise ValueError
                break
            except ValueError:
                print(
                    "Это не число. Попробуйте ещё раз!")
    elif f == 6:
        while True:
            try:
                unitec.loc[i, '1stCOGS'] = float(input("7/9. Какую сумму дополнительно тратите на первую сделку "
                                                       "(тестовый период, издержки на подключение клиента, etc.)? "
                                                       "Если не тратите, впишите ноль\n"))
                if unitec.loc[i, '1stCOGS'].dtype is 'string':
                    raise ValueError
                break
            except ValueError:
                print(
                    "Это не число. Попробуйте ещё раз!")
    elif f == 7:
        while True:
            try:
                unitec.loc[i, 'AvPaymentCount'] = float(
                    input("8/9. Сколько в среднем покупок у вашего клиента за период жизни?\n"))
                if unitec.loc[i, 'AvPaymentCount'].dtype is 'string':
                    raise ValueError
                break
            except ValueError:
                print(
                    "Это не число. Попробуйте ещё раз!")
    elif f == 8:
        while True:
            try:
                unitec.loc[i, 'Cost per Acquisition'] = float(
                    input("9/9. Сколько платите за привлечение одного пользователя?\n"))
                if unitec.loc[i, 'Cost per Acquisition'].dtype is 'string':
                    raise ValueError
                break
            except ValueError:
                print(
                    "Это не число. Попробуйте ещё раз!")
    else:
        pass


def calculating(i):
    unitec.loc[i, 'Buyers'] = unitec.loc[i, 'User Aquisition'] * unitec.loc[i, 'Convert to purchase']
    unitec.loc[i, 'AvPrice'] = unitec.loc[i, 'iPrice'] / unitec.loc[i, 'iCount']
    unitec.loc[i, 'Marketing cost'] = unitec.loc[i, 'User Aquisition'] * unitec.loc[i, 'Cost per Acquisition']
    unitec.loc[i, 'COGS, total'] = unitec.loc[i, 'AvPrice'] * unitec.loc[i, 'COGS, %'] + unitec.loc[i, 'COGS, fix']
    unitec.loc[i, 'AvRevenue per Customer'] = (unitec.loc[i, 'AvPrice'] - unitec.loc[i, 'COGS, total']) * \
                                              unitec.loc[i, 'AvPaymentCount'] - unitec.loc[i, '1stCOGS']
    unitec.loc[i, 'AvRevenue per User'] = unitec.loc[i, 'AvRevenue per Customer'] * unitec.loc[i, 'Convert to purchase']
    unitec.loc[i, 'Contribution Margin'] = unitec.loc[i, 'User Aquisition'] * (unitec.loc[i, 'AvRevenue per User'] -
                                                                               unitec.loc[i, 'Cost per Acquisition'])
    if unitec.loc[i, 'Contribution Margin'] > 0:
        print(
            'После вычета расходов, вы зарабатываете %.2f с %d пользователей.' % (unitec.loc[i, 'Contribution Margin'],
                                                                                  unitec.loc[i, 'User Aquisition']))
    elif unitec.loc[i, 'Contribution Margin'] < 0:
        print('После вычета расходов, вы в убытке на %.2f с %d пользователей' % (unitec.loc[i, 'Contribution Margin'],
                                                                                 unitec.loc[i, 'User Aquisition']))
    else:
        print('После вычета расходов, вы выходите в ноль')
    time.sleep(3)


def choose_step():
    while True:
        try:
            step = (int(
                input('1 -- Добавить расчёт на основе предыдущей строки \n2 -- Добавить новый расчёт \n'
                      '3 -- Скачать расчёт в формате .csv \n4 -- Выйти \n')))
            if step == 1:
                step_one()
            elif step == 2:
                step_two()
            elif step == 3:
                step_three()
            elif step == 4:
                step_four()
            else:
                raise Exception
            break
        except ValueError:
            print(
                "Это не число. Попробуйте ещё раз!")
        except Exception:
            print('Введите число от 1 до 4')


def step_one():
    global i
    i += 1
    unitec.loc[i] = unitec.loc[i - 1]

    def hyph_range(s):
        s = "".join(s.split())  # удаляет пробелы
        r = set()
        for x in s.split(','):
            t = x.split('-')
            if len(t) not in [1, 2]:
                raise SyntaxError("Допускается дефис только между двумя числами. Например: 5-8")
            r.add(int(t[0])) if len(t) == 1 else r.update(set(range(int(t[0]), int(t[1]) + 1)))
        l = list(r)
        l.sort()
        return l

    replace = hyph_range(input('Введите номера значений из предыдущего расчёта, которые хотите заменить. \n'
                               'Используйте запятую и дефис для перечисления. Пример: 1, 2-5\n'
                               '0 -- Количество пользователей \n1 -- Конверсия в первую покупку \n'
                               '2 -- Среднее количество товаров в корзине \n3 -- Средняя стоимость корзины \n'
                               '4 -- Долевая часть расходов от продажи \n5 -- фиксированные расходы от продажи \n'
                               '6 -- Дополнительные фиксированные расходы на первую покупку \n7 -- Среднее количество'
                               ' покупок клиента \n8 -- Расходы на привлечение одного пользователя \n'))
    for f in replace:
        ue_input(i, f)
    calculating(i)
    choose_step()


def step_two():
    global i
    i += 1
    for f in range(9):
        ue_input(i, f)
    calculating(i)
    choose_step()


def step_three():
    path = input('Введите путь к папке, в которую нужно сохранить файл\n')
    if path[-1] is '/':
        try:
            unitec.to_csv(r'{0}calculation-{1}.csv'.format(path, time.strftime("%Y-%m-%d-%H%M%S")))
            print('Файл сохранён')
            time.sleep(3)
        except FileNotFoundError:
            print('Не нашли эту папку. Попробуйте снова')
    else:
        try:
            unitec.to_csv(r'{0}/calculation-{1}.csv'.format(path, time.strftime("%Y-%m-%d-%H%M%S")))
            print('Файл сохранён')
            time.sleep(3)
        except FileNotFoundError:
            print('Не нашли эту папку. Попробуйте снова')
    choose_step()


def step_four():
    exit()


for f in range(9):
    ue_input(i, f)
calculating(i)
choose_step()
