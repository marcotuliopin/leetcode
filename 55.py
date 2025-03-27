from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0

        for pos, num in enumerate(nums):
            if pos > max_reach:
                return False
                
            max_reach = max(pos + num, max_reach)
            if max_reach >= len(nums) - 1:
                return True

        return True