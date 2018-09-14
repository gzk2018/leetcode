# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        nums = []
        def pre(root):
            if not root:return
            nums.append(root.val)
            pre(root.left)
            pre(root.right)
        pre(root)
        return nums