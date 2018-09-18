# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 2**31
        if not root:return 0
        def getdepth(root, d):
            if root.left is None and root.right is None:
                self.res = min(self.res, d)
            if root.left:
                getdepth(root.left, d + 1)
            if root.right:
                getdepth(root.right, d + 1)
        getdepth(root, 1)
        return self.res