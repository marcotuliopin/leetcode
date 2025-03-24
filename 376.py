from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        if len(nums) == 2:
            if nums[0] != nums[1]:
                return 2
            return 1

        ans = 2 if nums[1] != nums[0] else 1
        pattern = nums[1] - nums[0]

        for i in range(2, len(nums)):
            if (nums[i] - nums[i - 1] < 0 and pattern >= 0) or (nums[i] - nums[i - 1] > 0 and pattern <= 0):
                ans += 1
                pattern = nums[i] - nums[i - 1]
        return ans