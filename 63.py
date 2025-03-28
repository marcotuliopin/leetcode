from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[m - 1][n - 1] = obstacleGrid[m - 1][n - 1] ^ 1

        if not dp[m - 1][n - 1]:
            return 0
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if obstacleGrid[i][j] == 1:
                    continue
                dp[i][j] += dp[i + 1][j] + dp[i][j + 1]

        return dp[0][0]