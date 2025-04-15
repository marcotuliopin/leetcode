from collections import defaultdict
from typing import Counter, List


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        
        # Count of non-allocated numbers.
        counts = Counter(nums)
        # Each {key: value} pair represents the number of subsequences (value) that need the number (key).
        needs_num = defaultdict(int)
        for num in nums:
            # num has already been allocated in all existing subsequences.
            if counts[num] == 0:
                continue

            counts[num] -= 1

            # Add the number to the subsequence that needs it.
            if needs_num[num]:
                needs_num[num] -= 1
                needs_num[num + 1] += 1
            # If no existing subsequece needs this number, try creating a new one.
            elif counts[num + 1] and counts[num + 2]:
                counts[num + 1] -= 1
                counts[num + 2] -= 1
                needs_num[num + 3] += 1
            # Unable to create a new subsequece to fit the number.
            else:
                return False

        return True
