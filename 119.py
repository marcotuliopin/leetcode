from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        t = [1]

        for i in range(rowIndex):
            t.append(0)
            t[-1] = t[-2]
            for j in range(i, 0, -1):
                t[j] = t[j - 1] + t[j]
          
        return t