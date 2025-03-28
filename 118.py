from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        t = [[1]]

        for i in range(1, numRows):
            t.append([0] * (i + 1))
            t[i][0] = t[i - 1][0]
            t[i][-1] = t[i - 1][-1]

            for j in range(1, i):
                t[i][j] = t[i - 1][j - 1] + t[i - 1][j]
        return t