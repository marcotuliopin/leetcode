from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        ans = []
        q = deque()

        if root.val in to_delete:
            q.appendleft((root, False))
        else:
            q.appendleft((root, True))

        while q:
            node, is_root = q.pop()
            is_deleted = node.val in to_delete
            
            if is_root and not is_deleted:
                ans.append(node)
                
            if node.left:
                q.appendleft((node.left, is_deleted))
                if node.left.val in to_delete:
                    node.left = None
            if node.right:
                q.appendleft((node.right, is_deleted))
                if node.right.val in to_delete:
                    node.right = None
        return ans