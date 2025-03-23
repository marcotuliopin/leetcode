from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        dp = [1] * len(nums)
        max_idx = 0

        nums.sort()

        for i in range(len(nums)):
            for j in range(0, i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1    

                    if dp[i] > dp[max_idx]:
                        max_idx = i
        
        ans = [nums[max_idx]]
        count = dp[max_idx] - 1
        num = max_idx

        for i in range(max_idx - 1, -1, -1):
            if dp[i] == count and nums[num] % nums[i]  == 0:
                ans.append(nums[i])
                num = i
                count -= 1
        return ans[::-1]
        