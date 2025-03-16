from typing import List


class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        l = 1
        h = min(ranks) * cars ** 2

        while l <= h:
            m = (l + h) // 2

            c = 0
            for mech in ranks:
                c += int((m//mech) ** 0.5)
                if c >= cars:
                    break

            if c >= cars:
                h = m - 1
            else:
                l = m + 1

        return l
        