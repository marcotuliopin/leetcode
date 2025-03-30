from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.palindromes = {} 
        self.memo = {}
        
        return self.find_partitions(s)
    
    def find_partitions(self, s: str):
        if s in self.memo:
            return self.memo[s]

        if s == '':
            return [[]]
        
        self.memo[s] = []

        for i in range(len(s)):
            if not s[:i+1] in self.palindromes:
                self.palindromes[s[:i+1]] = self.is_palindrome(s[:i+1])
            
            if self.palindromes[s[:i+1]]:
                partitions = self.find_partitions(s[i+1:])

                for partition in partitions:
                    self.memo[s].append([s[:i+1]] + partition)

        return self.memo[s]

    def is_palindrome(self, s: str) -> bool:
        return s == s[::-1]