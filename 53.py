from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub = sub = nums[0]

        for i in range(1, len(nums)):
            if sub < 0:
                sub = 0
            sub += nums[i]
            max_sub = max(sub, max_sub)

        return max_sub 
        