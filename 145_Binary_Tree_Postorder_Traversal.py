# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        nums = []

        def post(root):
            if not root:return
            post(root.left)
            post(root.right)
            nums.append(root.val)
        post(root)
        return nums
