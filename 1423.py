from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if len(cardPoints) == k:
            return sum(cardPoints)

        # Find the least valuable subset of non-selected cards.
        least_valuable = sum(cardPoints[:-k])
        curr_score = least_valuable
        s = len(cardPoints) - k

        for i in range(k):
            curr_score = curr_score - cardPoints[i] + cardPoints[s+ i]
            least_valuable = min(least_valuable, curr_score)
        return sum(cardPoints) - least_valuable