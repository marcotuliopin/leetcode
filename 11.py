from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1

        container = 0

        while l < r:
            new_container = min(height[l], height[r]) * (r - l)
            container = max(container, new_container)
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return container