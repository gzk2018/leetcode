# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        self.res = True

        def inorder(p, q):
            if not p and not q:
                return
            elif not p:
                self.res = False
                return
            elif not q:
                self.res = False
                return
            if not (self.res and p.val == q.val):
                self.res = False
                return
            inorder(p.left, q.left)
            inorder(p.right, q.right)

        inorder(p, q)
        return self.res