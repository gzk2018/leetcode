# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.first = self.second = None
        self.pre = TreeNode(-2**31)
        def inorder(root):
            if not root:return
            inorder(root.left)
            if self.pre.val > root.val:
                if self.first is None:
                    self.first, self.second = self.pre, root
                else:
                    self.second = root
            # 在进入比自己大的节点之前赋值pre
            self.pre = root
            inorder(root.right)

        inorder(root)
        # 不能只交换first，要交换val
        self.first.val, self.second.val = self.second.val, self.first.val
