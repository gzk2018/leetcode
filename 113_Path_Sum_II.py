# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, Sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:return []
        self.res = []
        def dfs(root, path, s):
            if root.left is None and root.right is None:
                if s == Sum:
                    self.res.append(path)
                    return
            if root.left:dfs(root.left, path + [root.left.val], s + root.left.val)
            if root.right:dfs(root.right, path + [root.right.val], s + root.right.val)
        dfs(root,[root.val], root.val)
        return self.res