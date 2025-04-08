from collections import defaultdict
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
        
        total_len = len(nums)
        nums = set(nums)
        permutations = []

        def create_permutation(p, permutations, counter, nums):
            if len(p) == total_len:
                permutations.append(p)
                return

            for num in nums:
                if counter[num]:
                    counter[num] -= 1
                    create_permutation(p + [num], permutations, counter, nums)
                    counter[num] += 1

            
        create_permutation([], permutations, counter, nums)

        return permutations