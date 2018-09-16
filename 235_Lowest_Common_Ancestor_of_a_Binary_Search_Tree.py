# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p.val > q.val: p, q = q, p
        self.res = None

        def inorder(root):
            if not root or self.res != None: return
            if p.val <= root.val <= q.val:
                self.res = root
            inorder(root.left)
            inorder(root.right)

        inorder(root)
        return self.res
#
# s = Solution()
# a, b, c = TreeNode(2), TreeNode(6), TreeNode(8)
# e, f = TreeNode(0), TreeNode(4)
# a.left, a.right = e, f
# b.left, b.right = a, c
# res = s.lowestCommonAncestor(b, a, c)
# print(res.val)