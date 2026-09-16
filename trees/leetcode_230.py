# Definition for a binary tree node.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        n = k
        output = -1

        def inorder(root):
            nonlocal n, output

            if root is None:
                return 
            
            inorder(root.left)
            n -= 1
            if n == 0:
                output = root.val
                return 
            inorder(root.right)

        inorder(root)
        return output



        

        
        