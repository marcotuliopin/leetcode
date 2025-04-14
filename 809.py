from typing import List


class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def get_counts(word: str):
            counts = [1]
            sw = word[0]
            for char in word[1:]:
                if char != sw[-1]:
                    sw += char
                    counts.append(1)
                else:
                    counts[-1] += 1
            return sw, counts

        sw, counts = get_counts(s)

        ans = 0
        for word in words:
            nw, wc = get_counts(word)
            if nw != sw: continue

            add = True
            for c1, c2 in zip(counts, wc):
                if c2 > c1 or (c2 < c1 and c1 < 3):
                    add = False
                    break

            if add: ans += 1

        return ans
             
