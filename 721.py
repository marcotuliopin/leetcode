from collections import defaultdict, deque
from typing import List

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        g = defaultdict(list)

        for i, account in enumerate(accounts):
            for email in account[1:]:
                g[email].append(i)


        ans = []
        visited = set()
        for key in g.keys():
            if key in visited:
                continue

            q = deque()
            q.appendleft(key)
            visited.add(key)
            ans.append([accounts[g[key][0]][0]])

            while q:
                node = q.pop()
                ans[-1].append(node)

                for i in g[node]:
                    account = accounts[i]
                    for email in account[1:]:
                        if not email in visited:
                            visited.add(email)
                            q.appendleft(email)

            ans[-1][1:] = sorted(ans[-1][1:])
            
        return ans