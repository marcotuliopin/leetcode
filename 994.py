from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

        time = 0
        fresh = 0
        q = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
                elif grid[i][j] == 1:
                    fresh += 1
        
        if fresh == 0:
            return 0
        if not q:
            return -1
        
        while q:
            i, j, t = q.popleft()

            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1:
                    grid[x][y] = 2
                    q.append((x, y, t + 1))
                    time = max(t, t + 1)

        for row in grid:
            if 1 in row:
                return -1

        return time