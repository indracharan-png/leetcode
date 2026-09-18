# Definition for a binary tree node.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:

        output = float('-inf')

        def postOrder(root: Optional[TreeNode]) -> int:

            nonlocal output 

            # Base case 
            if root is None:
                return 0
            
            # Compute the max path sum from left subtree
            left_val = postOrder(root.left)
            # Compute the max path sum from right subtree
            right_val = postOrder(root.right)

            # Consider whichever is the greatest b/w left and right subtree max path sum values
            max_val = max(left_val, right_val, 0) # Check if max_val is decreasing the actual root value or not

            
            max_val = max(max_val, 0)

            # Update the output (the path could go starting some where in left subtree upto the root and then strech into some node in right sub tree)
            output = max(output, root.val + max(left_val, 0) + max(right_val, 0)) 

            return root.val + max_val


        postOrder(root)
        return int(output)
  


        