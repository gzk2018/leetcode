# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        self.res = True

        def judge(root, left, right):
            if not (self.res and left < root.val < right):
                self.res = False
                return

            if root.left:
                judge(root.left, left, root.val)
            if root.right:
                judge(root.right, root.val, right)

        judge(root, -float('inf'), float('inf'))
        return self.res