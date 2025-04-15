from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        hand.sort()

        while hand:
            size = 0
            idx = len(hand) - 1
            next_num = hand[-1]

            while size < groupSize:
                if not hand or idx < 0:
                    return False

                if hand[idx] == next_num:
                    next_num = hand.pop(idx) - 1
                    size += 1
                elif hand[idx] < next_num:
                    return False

                idx -= 1

        return True