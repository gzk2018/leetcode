# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:return []
        res = []
        def dfs(root, path):
            if not root.left and not root.right:
                res.append(path)
                return
            if root.left:dfs(root.left, path + '->' + str(root.left.val))
            if root.right:dfs(root.right, path + '->' + str(root.right.val))
        dfs(root, str(root.val))
        return res
