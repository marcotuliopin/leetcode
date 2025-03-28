class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False
        if not s3:
            return True
        
        if len(s1) < len(s2): 
            s1, s2 = s2, s1

        dp = [False] * (len(s2) + 1)
        dp[0] = True

        for i2 in range(1, len(s2) + 1):
            dp[i2] = dp[i2 - 1] and s2[i2 - 1] == s3[i2 - 1]
        
        for i1 in range(len(s1)):
            dp[0] = dp[0] and s1[i1] == s3[i1]

            for i2 in range(1, len(s2) + 1):
                dp[i2] = (dp[i2 - 1] and s2[i2 - 1] == s3[i1 + i2]) or (dp[i2] and s1[i1] == s3[i1 + i2])
        
        return dp[-1]