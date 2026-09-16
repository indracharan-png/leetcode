from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        index_of = {}
        # Set up the indices map for the preorder array
        n = len(inorder)
        for i in range(n):
            index_of[inorder[i]] = i

        def makeTree(preorder, pre_left, pre_right, inorder, in_left, in_right) -> Optional[TreeNode]:
            # Base case
            if in_left > in_right:
                return None
            
            # The element at the start of preorder sub-array will always be the root element (preorder:- root:left:right)
            new_node = TreeNode(preorder[pre_left])
            in_order_index = index_of[new_node.val] # Found out its index in inorder array using dict
            # Now all the elements residing left of index of root will be in left sub-tree (inorder:- left:root:right)
            left_len = in_order_index - in_left
            # Same as above all the elements residing right of index of root will be in right sub-tree (inorder:- left:root:right)
            right_len = in_right - in_order_index

            # Update the next left and right recursive function calls accordingly
            new_node.left = makeTree(preorder, pre_left + 1, pre_left + left_len, inorder, in_left, in_order_index - 1)
            new_node.right = makeTree(preorder, pre_left + left_len + 1, pre_right, inorder, in_order_index + 1, in_right)

            return new_node

        return makeTree(preorder, 0, n - 1, inorder, 0, n - 1)

    # Time-complexity: O(n): building dict + O(n): processing each node in makeTree function = O(n)
    # Space-complexity: O(n): for the dict + O(h): Recursion stack call space, h = height of tree = O(n)

          