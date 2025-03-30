from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda l: l[0])

        ans = [intervals[0]]

        for interval in intervals[1:]:
            if ans[-1][1] >= interval[0]: # Has overlap
                ans[-1][1] = max(ans[-1][1], interval[1])
            else:
                ans.append(interval)
        return ans