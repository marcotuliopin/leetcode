from collections import defaultdict
from typing import List


class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        counts = defaultdict(int)

        dominant = 0
        for num in nums:
            counts[num] += 1
            if counts[num] > len(nums) // 2:
                dominant = num
                break
        
        count = 0
        for i in range(len(nums)):
            if nums[i] == dominant:
                count += 1
            if count > (i + 1) // 2 and counts[dominant] - count > (len(nums) - i + 1) // 2:
                return i
        return -1
        

    