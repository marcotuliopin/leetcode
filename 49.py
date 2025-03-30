from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            sorted_str = sorted(s)
            if sorted_str not in anagrams:
                anagrams[sorted_str] = []

            anagrams[sorted_str].append(s)

        return list(anagrams.values())