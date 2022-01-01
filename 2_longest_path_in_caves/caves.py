
from typing import List

'''
Дан массив пещерных ходов cave.
Значения в массиве указывают номер пещеры,
куда из текущей пещеры можно пройти.

Например, cave[2, 2, 1]
означает, что пещеры с индексом 0 и 1 пути ведут в пещеру с индексом 2.
А из cave[2] можно попасть в cave[1].

Определите индекс пещеры, из которой будет самый длинный путь до
элемента массива со значением -1.

Ввод:
cave - целочисленный массив пещер, 1<length(cave)<=10

Вывод:
Integer - индекс в массиве, из которого будет самый длинный путь

Пример:
cave = [1, 2, -1]
get_result(cave) = 0
С нулевого индекса переход ведёт в первый, из первого - во второй.
Это самый длинный "путь" до нужного элемента.
'''


class Path:
    def __init__(self, the_cave) -> None:
        self.EXIT_CAVE = -1
        self.visited_caves = []
        self.length = 0
        self.first_cave = the_cave
        self.last_cave = the_cave

    def add_cave(self, the_cave: int):
        self.length += 1
        self.visited_caves.append(the_cave)
        self.last_cave = the_cave

    def is_finished(self) -> bool:
        return self.last_cave == self.EXIT_CAVE

    def __repr__(self) -> str:
        path = " -> ".join(map(str, self.visited_caves))
        return '{total}: {path}'.format(total=len(self.visited_caves), path=path)

    def __lt__(self, other) -> bool:
        return self.length < other.length


class LimitedPath(Path):
    def __init__(self, the_cave: int, the_limit: int) -> None:
        Path.__init__(self, the_cave)
        self.limit = the_limit

    def add_cave(self, the_cave: int):
        if self.length > self.limit:
            raise OverflowError
        return super().add_cave(the_cave)


class Caves:
    def __init__(self, the_caves: List[int]) -> None:
        self.caves = the_caves
        self.total_caves = len(self.caves)

    def getPathLenForCave(self, the_cave: int) -> Path:
        path = LimitedPath(the_cave, self.total_caves)

        while not path.is_finished():
            next_cave = self.caves[path.last_cave]
            try:
                path.add_cave(next_cave)
            except OverflowError:
                path = LimitedPath(-1, 1)

        return path

    def findStartPointForLongestPath(self) -> int:
        paths: list[Path] = []

        for cave_number in range(0, len(self.caves)):
            current_path = self.getPathLenForCave(cave_number)
            paths.append(current_path)

        paths.sort(key=lambda item: item.length)
        longest_path = paths.pop()
        return longest_path.first_cave


def get_result(the_caves: List[int]) -> int:
    my_caves = Caves(the_caves)
    return my_caves.findStartPointForLongestPath()
