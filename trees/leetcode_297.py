from typing import Optional


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left: Optional["TreeNode"] = None
        self.right: Optional["TreeNode"] = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # The idea is to go with preorder traversal as it preserves the ordering of nodes in trees. But make sure to consider 'None' values
        def preOrder(root) -> str:
            if root is None:
                return '#'
            curr_str = str(root.val)
            curr_str = curr_str + "," + preOrder(root.left)
            curr_str = curr_str + "," + preOrder(root.right)
            return curr_str

        return preOrder(root)
            
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        node_list = data.split(",")
        curr_idx = 0

        def constructBinaryTree(node_list) -> Optional[TreeNode]:
            nonlocal curr_idx

            if node_list[curr_idx] == '#':
                curr_idx +=1
                return None

            new_tree_node = TreeNode(int(node_list[curr_idx]))
            curr_idx += 1
            new_tree_node.left = constructBinaryTree(node_list)
            new_tree_node.right = constructBinaryTree(node_list)
            return new_tree_node

        return constructBinaryTree(node_list)
            
            
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))