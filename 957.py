from typing import List


class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        states = {}
        curr = int(''.join(str(i) for i in cells), 2)

        while n:
            states[curr] = n

            num = 0
            for i in range(1, 7):
                if (curr >> (i - 1)) & 1 == (curr >> (i + 1)) & 1:
                    num = num | (1 << i)

            n -=1
            curr = num

            if curr in states:
                n %= states[curr] - n


        ans = [(curr >> i) & 1 for i in range(7, -1, -1)]
        return ans