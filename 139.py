from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = {}
        return self.canBreak(s, wordDict, cache)
    
    def canBreak(self, s, wordDict, cache):
        if s in wordDict:
            return True
        
        if s in cache:
            return cache[s]
        
        for i in range(len(s)):
            prefix = s[:i]
            suffix = s[i:]

            if prefix in wordDict:
                cache[prefix] = True

            if prefix in cache and cache[prefix] and self.canBreak(suffix, wordDict, cache):
                cache[s] = True
                return True

        cache[s] = False
        return False
        