from collections import deque
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == '0000':
            return 0
        if '0000' in deadends:
            return -1

        q = deque()
        q.appendleft(('0000', 0))
        vis = set(['0000'])
        deadends = set(deadends)
        
        while q:
            config, d = q.pop()
            
            for i in range(4):
                s = config[:i] + str((int(config[i]) + 1) % 10) + config[i + 1:]

                if s in vis or s in deadends: continue
                vis.add(s)

                if s == target:
                    return d + 1

                q.appendleft((s, d + 1))

            for i in range(4):
                s = config[:i] + str((int(config[i]) - 1) % 10) + config[i + 1:]

                if s in vis or s in deadends: continue
                vis.add(s)

                if s == target:
                    return d + 1

                q.appendleft((s, d + 1))
            
        return -1