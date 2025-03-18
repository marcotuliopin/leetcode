class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[0] * len(s) for _ in range(len(s))]           
        max_palindrome = 0
        ans = ""

        for i in range(len(s)):
            dp[i][i] = 1
            for j in range(i):
                if s[i] != s[j]:
                    continue
                if dp[i - 1][j + 1] > 0:
                    dp[i][j] = dp[i - 1][j + 1] + 2
                    if max_palindrome < dp[i][j]:
                        max_palindrome = dp[i][j]
                        ans = s[i:j + 1]
                    
        return ans