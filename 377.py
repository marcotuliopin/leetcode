from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        def countCombinations(target, nums, dp):
            if target in dp:
                return dp[target]
            if target == 0:
                return 1

            combinations = 0
            for num in nums:
                if num > target: 
                    break

                combinations += countCombinations(target - num, nums, dp)

            dp[target] = combinations
            return dp[target]

        nums.sort()
        dp = {}

        return countCombinations(target, nums, dp)