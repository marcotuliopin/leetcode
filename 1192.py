from typing import List


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        self.time = 0
        lowlink = [-1] * n
        indexes = [-1] * n
        bridges = []
        adj = [[] for _ in range(n)]

        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(u, parent):
            indexes[u] = lowlink[u] = self.time
            self.time += 1

            for v in adj[u]:
                if v == parent:
                    continue

                if indexes[v] == -1:
                    dfs(v, u)

                if indexes[u] < lowlink[v]:
                    bridges.append([u, v])
                else:
                    lowlink[u] = min(lowlink[u], lowlink[v])
            return

        for u, idx in enumerate(indexes):
            if idx == -1:
                dfs(u, None)

        return bridges