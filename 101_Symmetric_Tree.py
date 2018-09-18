# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        self.res = True

        def issym(l, r):
            if not l and not r:
                return
            elif (not l and r) or (l and not r):
                self.res = False
                return

            if not (self.res and l.val == r.val):
                self.res = False
                return
            issym(l.left, r.right)
            issym(l.right, r.left)

        issym(root.left, root.right)
        return self.res