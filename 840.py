from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def is_magic(square: List[List[int]]) -> bool:
            if list(set([item for row in square for item in row])) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                return False
            magic_sum = sum(square[0])

            if not all(sum(row) == magic_sum for row in square[1:]):
                return False

            for col in range(3):
                if sum(square[row][col] for row in range(3)) != magic_sum:
                    return False
            
            if sum(square[i][i] for i in range(3)) != magic_sum:
                return False

            if sum(square[i][2 - i] for i in range(3)) != magic_sum:
                return False

            return True
            
        ans = 0
        
        for i in range(len(grid) - 2):
            for j in range(len(grid[0]) - 2):
                if is_magic([row[j:j + 3] for row in grid[i:i + 3]]):
                    ans += 1
        return ans
        