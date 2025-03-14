from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        chars_idxs = {}
        intervals = []
        results = []

        idx = 0
        for i, c in enumerate(s):
            if c not in chars_idxs:
                intervals.append([i, i])
                chars_idxs[c] = idx
                idx += 1
            else:
                intervals[chars_idxs[c]][1] = i

        results.append(intervals[0])
        for i in range(1, len(intervals)):
            if intervals[i][0] <= results[-1][1]:
                results[-1][1] = max(results[-1][1], intervals[i][1])
            else:
                results.append(intervals[i])
        
        return [interval[1] - interval[0] + 1 for interval in results]