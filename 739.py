from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        data = [-1] * 100
        ans = [0] * len (temperatures)

        for i in range(len(temperatures) - 1, -1, -1):
            data[temperatures[i]] = i

            minWait = len(temperatures) + 1
            for j in range(i + 1, len(data)):
                if data == -1:
                    continue
                minWait = min(data[j], minWait)

            if minWait < len(temperatures) + 1:
                ans[i] = i - minWait

        return ans
            