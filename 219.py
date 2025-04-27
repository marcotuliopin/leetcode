from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_occurrence = {}

        for i, num in enumerate(nums):
            if num in last_occurrence and i - last_occurrence[num] <= k:
                return True
            last_occurrence[num] = i
        return False