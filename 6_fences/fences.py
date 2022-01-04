
from typing import List
from itertools import permutations
'''
Вы играете в игру, где ваш персонаж прыгает по заборчикам.
Значения в массиве означают, сколько заборчиков персонаж
обязан перешагнуть, двигаясь вперед.
Вы можете менять элементы в массиве местами.

Чтобы выиграть, персонажу нужно дойти до финиша,
в нашем случае - это добраться до последнего индекса массива.
Выведите true, если победить в игре возможно,
в противном случае - false.

Ввод:
* fences - массив значений длин прыжков.

Герой начинает с нулевого индекса,
1<length(fences)<=20,
-10<=fences[i]<=15

Вывод:
Boolean - возможно ли победить

Example:
fences = [0, 2, 4, 1, 6, 2]
get_result(fences) = True

Один из возможных вариантов: [1, 4, 2, 0, 6, 2].
Герой с 0-го индекса прыгнул на 1-ый,
и сразу же смог прыгнуть на последний индекс
массива - он победил
'''


class FenceWay:
    def __init__(self, the_way_points) -> None:
        self.way_points = the_way_points
        self.current_fence_index = 0
        self.target_fence = len(self.way_points) - 1

    def canReachTheLastFence(self):
        for next_way_point in self.way_points:
            if next_way_point == 0:
                return False

            self.current_fence_index += next_way_point

            if self.isInTargetFence():
                return True

            if not self.isValidPosition():
                return False

    def isValidPosition(self):
        if self.current_fence_index < 0:
            return False
        if self.current_fence_index > self.target_fence:
            return False
        return True

    def isInTargetFence(self):
        return self.current_fence_index == self.target_fence

    def __repr__(self) -> str:
        return 'FenceWay: {}'.format(self.way_points)


class FenceWalker:
    def __init__(self, the_fences: List[int]) -> None:
        self.fences = the_fences

    def canGoToTheLastFence(self) -> bool:

        all_ways = list(permutations(self.fences))
        for current_fences in all_ways:
            current_way = FenceWay(current_fences)
            can_reach_last_fence = current_way.canReachTheLastFence()
            if can_reach_last_fence:
                return True
        return False


def get_result(fences: List[int]):
    walker = FenceWalker(fences)
    return walker.canGoToTheLastFence()
