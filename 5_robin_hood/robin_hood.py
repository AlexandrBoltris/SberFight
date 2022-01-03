
'''
Доблестный или почти доблестный Робин Гуд и
отправляетесь в новый поход в лес.

Дан массив passersby, в котором содержится
количество золотых у каждого путника в лесу,
которого можно обокрасть.
В результате кражи все деньги путника переходят к Робину.

Но, каждый раз после того как совершена кража,
Робин обязан отдать часть денег другому путнику,
иначе его будут считать просто вором.

Для очищения совести достаточно
умножить сумму золотых прохожего вдвое, то есть,
выгоднее всего отдавать деньги бедным.

Робин Гуд волен сам выбирать у какого путника
будет красть золотые, он также вправе
не трогать проходящего человека.

Главная задача Робина Гуда - оставить максимальное
количество золотых себе, найдите это количество.

Ввод:
* passersby - массив прохожих, где
passerby[i] - количество золотых прохожего i,
0<length(passerby)<=10, 0<passerby[i]<1000

Вывод:
* Integer - количество золотых, которые остались у Робин Гуда

Пример:
passersby = [3, 10, 4, 8]
get_result(passersby) = 11

Робин Гуд обокрал путников с 10 и 8 золотыми и
одарил остальных двух на 3 и 4 золотых соответственно.
То есть 10+8-3-4
'''


def get_result(passersby):
    passersby.sort()

    total_passerbys = len(passersby)
    passerbys_to_visit = len(passersby) // 2

    total_money = 0

    # take money phase
    for current_passerby in range(total_passerbys-passerbys_to_visit, total_passerbys):
        total_money += passersby[current_passerby]

    # give money phase
    for current_passerby in range(0, passerbys_to_visit):
        total_money -= passersby[current_passerby]

    return total_money
