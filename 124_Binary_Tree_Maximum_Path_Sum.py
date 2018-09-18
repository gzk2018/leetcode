# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = -2**31
        if not root:return 0
        def helper(root):
            if not root:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            res = max(root.val, max(left, right) + root.val)
            self.res = max(self.res, res, root.val + left + right)
            return res
        helper(root)
        return self.res