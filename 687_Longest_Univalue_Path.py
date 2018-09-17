# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        def helper(root):
            if not root:
                return 0
            left_in = right_in = 0
            left = helper(root.left)
            right = helper(root.right)
            if root.left and root.val == root.left.val:
                left_in = left + 1
            if root.right and root.val == root.right.val:
                right_in = right + 1
            self.res = max(self.res, left_in + right_in)
            return max(left_in, right_in)
        helper(root)
        return self.res