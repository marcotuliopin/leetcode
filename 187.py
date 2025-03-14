from collections import defaultdict
from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        hash_map = defaultdict(int)
        result = []

        for i in range(len(s) - 9):
            sequence = s[i:i + 10]
            if sequence in hash_map and hash_map[sequence] == 1:
                print(sequence)
                result.append(sequence)
            else:
                hash_map[sequence] += 1
        return result