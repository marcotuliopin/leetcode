from collections import defaultdict
import re
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        counts = defaultdict(int)
        most_frequent = ""

        paragraph = re.sub("[!?',;.]", " ", paragraph)
        paragraph = paragraph.lower()
        paragraph = paragraph.split()

        banned = set(banned)

        for word in paragraph:
            if word in banned:
                continue
            counts[word] += 1
            if counts[word] > counts[most_frequent]:
                most_frequent = word
        return word


