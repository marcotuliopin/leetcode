from collections import Counter
from typing import List


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        def gcd(freqs):
            for i in range(2, min(freqs) // 2 + 1):
                if all(freq % i == 0 for freq in freqs):
                    return True
            if min(freqs) > 1 and all(freq % min(freqs) == 0 for freq in freqs):
                return True

            return False
                    
        count = Counter(deck)
        if gcd(count.values()):
            return True

        return False