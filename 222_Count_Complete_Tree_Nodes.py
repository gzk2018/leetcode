# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left, right = root.left, root.right
        l = r = 0
        while left:
            l += 1
            left = left.left
        while right:
            r += 1
            right = right.left
        if l == r:
            return 2 ** l + self.countNodes(root.right)
        else:
            return 2 ** r + self.countNodes(root.left)


