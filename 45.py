from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        end, jumps, farthest = 0, 0, 0

        for i, num in enumerate(nums[:-1]):
            end = max(end, i + num)
            # Only update jump counts after we checked every possible jump before the 
            # last best one.
            if i == farthest:
                jumps += 1
                farthest = end
            
        return jumps