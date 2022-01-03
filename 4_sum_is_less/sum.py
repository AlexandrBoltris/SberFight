from typing import List
from copy import deepcopy


'''На вход подается числовой массив.
За одну операцию вы можете разделить любое число в массиве
на два (целочисленное деление).

Определите, может ли сумма всех элементов в массиве
быть не больше w.

Общее количество операций не должно превышать значение
самого большого числа в массиве.

Возможное общее количество операций меняется динамически,
то есть если Вы будете делить самое крупное число,
то общее количество возможных операций уменьшится.

Ввод:
* arr - массив чисел (integer[]), 1<length(arr)<10
* w - число, максимальный предел для суммы массива (integer), 0<w<100

Вывод:
Boolean - возможно ли удовлетворить условие sum(arr) <= w

Пример:
arr = [3, 2, 4, 5]
W = 9
get_result(arr, W) = true

Сначала количество возможных операций равно 5
(самое большое число в исходном массиве)
5 // 2 = 2 [3, 2, 4, 2], теперь количество проведенных
операций равно 1, а число возможных операций - 4
4 // 2 = 2 [3, 2, 2, 2], теперь количество проведенных
операций равно 2, а число возможных операций - 3
Уже сейчас выполняется условие: 3 + 2 + 2 + 2 <= 9
'''


class Solution:
    '''Warning! Soution uses python's deepcopy()
    in order to check sum of values in the future.
    You have to think 7 times before do the same thing in production.
    This code is writted to run just ONE time,
    and I don't want to spend more time for it.
    Especially I will not get more points for a solution without a deepcopy()'''

    def __init__(self, the_values: List[int]) -> None:
        self.values = the_values
        self.values.sort(reverse=True)
        self.updateStepsLimit()
        self.step_counter = 0

    def findMinumumSum(self) -> int:
        while not self.isFinished():
            index_to_devide = self.findBestIndexToDevive()
            self.devide(index_to_devide)
        return self.getSum()

    def isFinished(self) -> bool:
        return self.step_counter >= self.step_limit

    def canDevideHead(self) -> bool:
        temp = deepcopy(self)
        temp.devide(0)
        return temp.step_limit > temp.step_counter

    def getSum(self):
        return sum(self.values)

    def updateStepsLimit(self):
        self.step_limit = max(self.values)

    def devide(self, the_index):
        self.values[the_index] = self.values[the_index] // 2
        self.values.sort(reverse=True)
        print(self.step_counter, the_index, self.values)
        self.updateStepsLimit()
        self.step_counter += 1

    def calculateDeltaForHead(self):
        temp = deepcopy(self)
        temp.devide(0)
        return self.getSum() - temp.getSum()

    def calculateDeltaForTail(self):
        temp = deepcopy(self)

        number_of_steps = self.values[0] // 2
        for i in range(0, number_of_steps):
            temp.devide(1)

        return self.getSum() - temp.getSum()

    def findBestIndexToDevive(self) -> int:
        if self.canDevideHead():
            delta_for_head = self.calculateDeltaForHead()
            delta_for_tail = self.calculateDeltaForTail()
            if delta_for_head > delta_for_tail:
                return 0
            else:
                return 1
        else:
            return 1


def get_result(arr, w):
    solution = Solution(arr)
    minimumSum = solution.findMinumumSum()
    return minimumSum <= w
