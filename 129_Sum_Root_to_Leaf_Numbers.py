# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        res = []
        def func(root, digits):
            digits = digits*10 + root.val
            if not root.left and not root.right:
                res.append(digits)
                return
            if root.left:
                func(root.left, digits)
            if root.right:
                func(root.right, digits)
        func(root, 0)
        return sum(res)