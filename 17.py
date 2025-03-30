from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
            
        s = [('', 0)]
        ans = []

        while s:
            comb, pos = s.pop()
            if pos >= len(digits):
                ans.append(comb)
                continue

            for i in range(len(mapping[digits[pos]])):
                s.append((comb + mapping[digits[pos]][i], pos + 1))

        return ans