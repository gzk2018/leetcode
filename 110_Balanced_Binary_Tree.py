# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        def getdepth(root):
            # 如果没有子结点，那么深度为1，不是0
            if not root.left and not root.right:
                return 1
            left = right = 0
            if root.left:
                left = getdepth(root.left)
            if root.right:
                right = getdepth(root.right)

            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            else:
                return 1 + max(right, left)

        return getdepth(root) != -1