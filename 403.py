from typing import List


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if len(stones) > 1 and stones[1] > 1:
            return False
        dp = [[] for _ in range(len(stones))]
        dp[1].extend([1, 2])

        for i in range(len(stones)):
            for j in range(0, i):
                k = stones[i] - stones[j]
                if k in dp[j]:
                    dp[i].extend([k - 1, k, k + 1])

        return bool(dp[-1]) 