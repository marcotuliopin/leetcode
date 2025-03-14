from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        l, r = 0, len(height) - 1
        hl, hr = height[0], height[-1]

        while l < r:
            if hl < hr:
                l += 1
                hl = max(hl, height[l])
                water += hl - height[l]
            else:
                r -= 1
                hr = max(hr, height[r])
                water += hr - height[r]
        return water


# Runtime exceeded.
class Solution:
    def trap(self, height: List[int]) -> int:
        max_height = max(height)
        water = 0

        for i in range(max_height, 0, -1):
            l = -1
            for j in range(len(height)):
                if height[j] >= i:
                    if l == -1:
                        l = j
                    else:
                        water += j - l - 1
                        l = -1
        return water