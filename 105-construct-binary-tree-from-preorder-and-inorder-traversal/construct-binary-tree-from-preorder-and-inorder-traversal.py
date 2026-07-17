# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if not preorder or not inorder:
            return None

        # First element of preorder is the root
        root_value = preorder[0]
        root = TreeNode(root_value)

        # Find root's position in inorder
        root_index = inorder.index(root_value)

        # Left subtree
        left_inorder = inorder[:root_index]

        # Right subtree
        right_inorder = inorder[root_index + 1:]

        # Build left subtree
        root.left = self.buildTree(
            preorder[1:root_index + 1],
            left_inorder
        )

        # Build right subtree
        root.right = self.buildTree(
            preorder[root_index + 1:],
            right_inorder
        )

        return root