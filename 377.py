from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        def countCombinations(target, nums, dp):
            if target in dp:
                return dp[target]

            combinations = 0
            for num in nums:
                if num > target: 
                    break

                if num == target:
                    combinations += 1
                else:
                    combinations += countCombinations(target - num, nums, dp)

            dp[target] = combinations
            return dp[target]

        nums.sort()
        dp = {}

        return countCombinations(target, nums, dp)