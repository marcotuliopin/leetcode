from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            twosum = {}
            for j in range(i + 1, len(nums)):
                if nums[j] in twosum:
                    ans.add((nums[i], nums[j], nums[twosum[nums[j]]]))
                twosum[-nums[i] - nums[j]] = j
        return list(ans)