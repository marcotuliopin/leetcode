from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

        def bfs(grid: List[List[str]], row: int, col: int) -> None:
            q = deque()
            q.append((row, col))

            while q:
                row, col = q.popleft()

                grid[row][col] = "0"

                for (dy, dx) in directions:
                    if row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0]) and grid[row + dy][col + dx] == "1":
                        grid[row + dy][col + dx] = "0"
                        q.append((row + dy, col + dx))

        num = 0

        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val != "1":
                    continue

                num += 1
                bfs(grid, i, j)

        return num
