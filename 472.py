from typing import List


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        def is_concatenated(word, dictionary, cache):
            if word in cache:
                return cache[word]

            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]

                if prefix in dictionary:
                    if suffix in dictionary or is_concatenated(suffix, dictionary, cache):
                        cache[word] = True
                        return True
            cache[word] = False
            return False


        dictionary = set(words)
        concatenated = set()
        cache = {}

        for word in words:
            if not word in concatenated and is_concatenated(word, dictionary, cache):
                concatenated.add(word)
        return list(concatenated)
        