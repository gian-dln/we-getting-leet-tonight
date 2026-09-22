from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# bfs solution
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        visited = deque([root])
        while visited:
            node = visited.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                visited.append(node.left)
            if node.right:
                visited.append(node.right)
        return root