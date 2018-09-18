# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:return 0
        self.depth = 0
        def dfs(root, d):
            if not root.left and not root.right:
                self.depth = max(self.depth, d)
                return
            if root.left:
                dfs(root.left, d + 1)
            if root.right:
                dfs(root.right, d + 1)
        dfs(root, 1)
        return self.depth