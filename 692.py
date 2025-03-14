from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        map = defaultdict(int)

        for word in words:
            map[word] += 1
        
        return sorted(map, key=lambda x: (-map[x], x))[:k]