
from typing import List, Tuple

'''
Дан массив чисел array_start.
Вы можете менять местами элементы массива.
Ваша задача: получить array_goal.

Необходимо определить минимально возможное количество перемещений элементов массива,
которое требуется, чтобы получить нужный порядок в массиве.

Ввод:
* array_start - начальный массив, 1<length(array_start)<10
* array_goal - конечный массив, length(array_start)=length(array_goal)

Вывод:
* Integer

Пример:

array_start = [3, 2, 1, 4]
array_goal = [1, 2, 3, 4]
get_result(array_start, array_goal) = 1
Меняем 3 и 1 местами и получаем нужную последовательность в массиве.
'''


class Positions:
    def __init__(self) -> None:
        self.positions: List[int] = []

    def append(self, the_position: int):
        self.positions.append(the_position)

    def remove(self, the_position: int):
        self.positions.remove(the_position)

    def clear(self):
        self.positions.clear()

    def isEmpty(self) -> bool:
        return len(self.positions) == 0

    def get(self):
        return self.positions


class SwappableSolution:
    def __init__(self, the_start: List[int], the_goal: List[int]) -> None:
        self.current = the_start
        self.goal = the_goal
        self.bad_positions = Positions()
        self.swap_counter = 0
        self.updateBadPositions()

    def getSwapScore(self, first: int, second: int) -> int:
        '''The higher the better

        2: if TWO elements will be in their places after swaping first and second elements
        1: if ONE elemet will in it's place after swaping first and second element
        0: is swap makes no sense'''

        score = 0
        if self.goal[first] == self.current[second]:
            score += 1
        if self.goal[second] == self.current[first]:
            score += 1
        return score

    def updateBadPositions(self):
        self.bad_positions.clear()
        for i in range(0, len(self.goal)):
            if not self.areElementsEquals(i):
                self.bad_positions.append(i)

    def areElementsEquals(self, the_position: int) -> bool:
        return self.goal[the_position] == self.current[the_position]

    def getSwapsWithMaxScore(self) -> List[Tuple[int, int]]:
        MAX_SCORE = 2
        all_bad_positions = self.bad_positions.get()
        swapsWithGivenScore = []
        for i in range(0, len(all_bad_positions)):
            left = all_bad_positions[i]
            for right in all_bad_positions[i:]:
                if self.getSwapScore(left, right) == MAX_SCORE:
                    swapsWithGivenScore.append((left, right))
        return swapsWithGivenScore

    def doAllSwapsWithMaxScore(self):
        swaps = self.getSwapsWithMaxScore()
        for swap in swaps:
            self.doSwap(swap[0], swap[1])
            self.bad_positions.remove(swap[0])
            self.bad_positions.remove(swap[1])

    def doOneSwapWithMinScore(self):
        MIN_SCORE = 1
        all_bad_positions = self.bad_positions.get()

        for i in range(0, len(all_bad_positions)):
            left = all_bad_positions[i]
            for right in all_bad_positions[i:]:
                if self.getSwapScore(left, right) == MIN_SCORE:
                    self.doSwap(left, right)
                    self.updateBadPositions()
                    return 0  # only one swap here

    def getSwapCount(self) -> int:

        while not self.bad_positions.isEmpty():
            self.doAllSwapsWithMaxScore()
            self.doOneSwapWithMinScore()

        return self.swap_counter

    def doSwap(self, the_first: int, the_second: int):
        first_value = self.current[the_first]
        self.current[the_first] = self.current[the_second]
        self.current[the_second] = first_value

        self.swap_counter += 1


def get_result(array_start: List[int], array_goal: List[int]) -> int:

    if len(array_start) != len(array_goal):
        return 0

    swappeble_solution = SwappableSolution(array_start, array_goal)
    result = swappeble_solution.getSwapCount()
    return result
