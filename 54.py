from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        tsize = m * n

        up, down = 0, m - 1
        left, right = 0, n - 1

        ans = []

        while len(ans) < m * n:
            # l -> r
            ans.extend(matrix[up][left:right+1])
            up += 1
            if len(ans) >= tsize: break
            # u -> d
            for row in matrix[up:down+1]:
                ans.append(row[right])
            right -= 1
            if len(ans) >= tsize: break
            # r -> l
            ans.extend(matrix[down][left:right+1][::-1])
            down -= 1
            if len(ans) >= tsize: break
            # d -> u
            for row in matrix[up:down+1][::-1]:
                ans.append(row[left])
            left += 1
        return ans