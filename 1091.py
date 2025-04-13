from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        directions = [(1, 0), (0, 1), (1, 1), (-1, 0), (0, -1), (-1, -1), (1, -1), (-1, 1)]

        n = len(grid)
        distances = [[-1] * n for _ in range(n)]
        distances[0][0] = 1

        q = deque()
        q.appendleft((0, 0))

        while q:
            x, y, = q.pop()

            for dx, dy in directions:
                if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid):
                    if distances[x + dx][y + dy] != -1 or grid[x + dx][y + dy] == 1:
                        continue
                    distances[x + dx][y + dy] = distances[x][y] + 1
                    q.appendleft((x + dx, y + dy))

        return distances[-1][-1]