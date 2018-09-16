# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.count = 0
        self.res = None
        def inorder(root):
            if not root or self.res != None:
                return
            inorder(root.left)
            self.count += 1
            if self.count == k:
                self.res = root.val
            inorder(root.right)
        inorder(root)
        return self.res