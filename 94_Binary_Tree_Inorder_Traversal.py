# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.res = []

        def inorder(root):
            if not root: return
            inorder(root.left)
            self.res.append(root.val)
            inorder(root.right)

        inorder(root)
        return self.res