from typing import List, Set, Tuple, Deque

from collections import deque


class Array:
    def __init__(self, array: List[List[str]]):
        self.array = array
        self.rows = len(array)
        self.columns = len(array[0])


class CountIslands:
    neighbours: List[Tuple[int]] = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, 1), (1, -1), (1, 1), (-1, -1)]
    visited: Set[Tuple] = set()
    islands: int = 0

    def __init__(self, array: Array):
        self.array = array

    def breadth_first_search(self, row, col):
        q = deque()
        self.visited.add((row, col))
        q.append((row, col))
        while q:
            _r, _c = q.popleft()
            for x, y in self.neighbours:
                r, c = _r + x, _c + y
                if (r in range(self.array.rows) and c in range(self.array.columns) and
                        self.array.array[r][c] == "1" and (r, c) not in self.visited):
                    q.append((r, c))
                    self.visited.add((r, c))

    def count_islands(self):
        for row in range(self.array.rows):
            for col in range(self.array.columns):
                if self.array.array[row][col] == "1" and (row, col) not in self.visited:
                    self.breadth_first_search(row, col)
                    self.islands += 1
        return self.islands