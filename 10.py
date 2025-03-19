class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        self.dp = [[None] * 21 for _ in range(21)]
        return self.solve(s, p, 0, 0)
    
    def solve(self, s, p, i, j):
        if j >= len(p):
            return i >= len(s)

        if not self.dp[i][j] is None:
            return self.dp[i][j]

        if j + 1 < len(p) and p[j + 1] == '*':
            if i < len(s) and (s[i] == p[j] or p[j] == '.'):
                spend = self.solve(s, p, i + 1, j)
            else:
                spend = False
            dont_spend = self.solve(s, p, i, j + 2)
            
            self.dp[i][j] = spend or dont_spend
            return spend or dont_spend

        if i < len(s) and (s[i] == p[j] or p[j] == '.'):
            self.dp[i][j] = self.solve(s, p, i + 1, j + 1)
            return self.dp[i][j]

        self.dp[i][j] = False
        return False
                