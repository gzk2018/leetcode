# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        res = []
        level = [root]
        while level:
            nextlevel = []
            for index, node in enumerate(level):
                if node.left: nextlevel.append(node.left)
                if node.right: nextlevel.append(node.right)
                if index == len(level) - 1:
                    res.append(node.val)
            level = nextlevel
        return res
