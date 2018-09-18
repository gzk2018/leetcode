# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, Sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root: return False
        self.res = False

        def dfs(s, root):
            if self.res or (root.left is None and root.right is None):
                if s == Sum:
                    self.res = True
                return
            if root.left: dfs(s + root.left.val, root.left)
            if root.right: dfs(s + root.right.val, root.right)

        dfs(root.val, root)
        return self.res
