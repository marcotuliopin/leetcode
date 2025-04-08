class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not s:
            if not p or all(c == '*' for c in p):
                return True
            return False
        if not p:
            return False

        dp = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]

        cut = 0
        lastMatch = 0
        for i in range(0, len(p)):

            match = False
            for j in range(cut, lastMatch + 1):
                
                if p[i] == '*':
                    dp[i][j:] = [True] * len(s[j:])
                    lastMatch = len(s) - 1
                    break
                    
                if p[i] == '?' or p[i] == s[i]:
                    if not match:
                        cut += 1
                        match = True

                    dp[i][j] = True
                    lastMatch = j

            if not match:
                return False
                    

        return dp[-1][-1]