from typing import List, Tuple, Deque

from collections import deque


class Array:
    def __init__(self, array: List[List[str]]):
        self.array = array
        self.rows = len(array)
        self.columns = len(array[0])


class CountIslands:
    neighbours: List[Tuple[int]] = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, 1), (1, -1), (1, 1), (-1, -1)]
    islands: int = 0
    q: Deque = deque()

    def __init__(self, array: Array):
        self.array = array

    def breadth_first_search(self, row, col):
        self.array.array[row][col] = "2"  # mark as visited
        self.q.append((row, col))
        while self.q:
            _r, _c = self.q.popleft()
            for x, y in self.neighbours:
                r, c = _r + x, _c + y
                if r in range(self.array.rows) and c in range(self.array.columns) and self.array.array[r][c] == "1":
                    self.q.append((r, c))
                    self.array.array[r][c] = "2"  # mark as visited

    def count_islands(self):
        for row in range(self.array.rows):
            for col in range(self.array.columns):
                if self.array.array[row][col] == "1":
                    self.breadth_first_search(row, col)
                    self.islands += 1
        return self.islands
