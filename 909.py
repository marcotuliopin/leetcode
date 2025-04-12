from collections import deque
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        def get_position(i, n):
            row = -(i // n + 1)
            if row % 2 == 1:
                col = i % n
            else:
                col = n - (i % n + 1)
            return row, col

        m, n = len(board), len(board[0])
        vis = [False] * m * n

        q = deque()
        q.appendleft((0, 0))

        while q:
            pos, t = q.pop()

            if pos == m * n - 1:
                return t

            if vis[pos]:
                continue
            vis[pos] = True

            for d in range(1, 7):
                if pos + d >= m * n:
                    continue
                row, col = get_position(pos + d, n)
                if board[row][col] != -1:
                    q.appendleft((board[row][col] - 1, t + 1))
                else:
                    q.appendleft((pos + d, t + 1))
            
        return -1