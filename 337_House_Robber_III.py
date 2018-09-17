# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(root):
            if not root:
                return (0,0)
            left, left_in = helper(root.left)
            right, right_in = helper(root.right)
            # 包含的时候可以把左右节点不包含的都加上
            res_in = left + right + root.val
            # 不包含的时候找两边最大的
            res = max(left, left_in) + max(right, right_in)
            return res, res_in
        return max(helper(root))