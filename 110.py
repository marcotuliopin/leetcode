from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def solve(root):
            if not root:
                return True, 0
                
            r_balanced, r_height = solve(root.right)
            if not r_balanced:
                return False, 0
            l_balanced, l_height = solve(root.left)
            if not l_balanced:
                return False, 0

            if abs(l_height - r_height) <= 1:
                return True, max(l_height, r_height) + 1
            return False, 0
        
        is_balanced, _ = solve(root)
        return is_balanced