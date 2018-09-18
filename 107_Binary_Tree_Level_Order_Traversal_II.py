# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:return []
        level = [root]
        res = []
        while level:
            nextlevel = []
            val = []
            for node in level:
                val.append(node.val)
                if node.left:nextlevel.append(node.left)
                if node.right:nextlevel.append(node.right)
            res.append(val)
            level = nextlevel
        return res[::-1]