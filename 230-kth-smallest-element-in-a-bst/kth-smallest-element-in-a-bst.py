# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        result = []

        def inorder(node):
            if node is None:
                return

            # Visit left subtree
            inorder(node.left)

            # Store current node value
            result.append(node.val)

            # Visit right subtree
            inorder(node.right)

        inorder(root)

        return result[k - 1]