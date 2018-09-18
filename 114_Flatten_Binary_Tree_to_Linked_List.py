# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:return
        def helper(root):
            if not root:
                return
            # 先把左边list化
            helper(root.left)
            # 然后把左边的接到右边来
            # 原有的右结点接到左边的最后面的右结点上
            # 然后再递归list化右结点
            if root.left:
                tail = root.left
                while tail.right:
                    tail = tail.right
                temp = root.right
                root.right = root.left
                tail.right = temp
                root.left = None
            helper(root.right)
        helper(root)            