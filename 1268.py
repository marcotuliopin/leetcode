from bisect import bisect_left
from typing import List


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()

        ans = []
        prefix = ''
        
        for c in searchWord:
            prefix += c

            insertion_p = bisect_left(products, prefix)

            suggestions = []
            for i in range(3):
                p = insertion_p + i
                if p >= len(products) or not products[p].startswith(prefix):
                    break
                suggestions.append(products[p])
            ans.append(suggestions)

        return ans