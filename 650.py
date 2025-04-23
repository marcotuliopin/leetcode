class Solution:
    def minSteps(self, n: int) -> int:
        dp = [[n + 1] * (n + 1) for _ in range(n + 1)]
        dp[0][1] = 0

        ans = n + 1

        for i in range(n):
            for j in range(n - i + 1):
                dp[j][j] = min(dp[j][j], dp[i][j] + 1)
                if i + j <= n:
                    dp[i][i + j] = min(dp[i][i + j], dp[i][j] + 1)
                    if i + j == n:
                        ans = min(ans, dp[i][i + j])
        return ans