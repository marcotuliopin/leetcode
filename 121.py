from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        sm_price = 10e+5

        for p in prices:
            ans = max(ans, p - sm_price)
            sm_price = min(p, sm_price)
        return ans