from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        sum = 0

        def is_leaf(node: TreeNode) -> bool:
            if node.left == None and node.right == None:
                return True
            return False

        # Use a stack to turn iterative.
        def preorder(node: TreeNode) -> int:
            sum = 0

            if node.left:
                if is_leaf(node.left):
                    sum += node.left.val
                else:
                    sum += preorder(node.left)

            if node.right:
                sum += preorder(node.right)

            return sum
        
        sum = preorder(root)
        print(sum)
        return sum
        