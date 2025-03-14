from typing import List


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.mx = matrix

        for i in range(len(self.mx)):
            for j in range(len(self.mx[0])):
                val = 0

                if j - 1 >= 0:
                    val += self.mx[i][j - 1]
                if i - 1 >= 0:
                    val += self.mx[i - 1][j]

                if i - 1 >= 0 and j - 1 >= 0:
                    val -= self.mx[i - 1][j - 1]
                
                val += self.mx[i][j]
                    
                self.mx[i][j] = val

        print(self.mx[0])
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int: 
        ans = self.mx[row2][col2]
        if row1 > 0:
            ans -= self.mx[row1 - 1][col2]
        if col1 > 0:
            ans -= self.mx[row2][col1 - 1]
        
        if row1 > 0 and col1 > 0:
            ans += self.mx[row1 - 1][col1 - 1]
        return ans

obj = NumMatrix([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]])