# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0: return []
        nums = [i + 1 for i in range(n)]

        def generate(nums):
            if not nums:
                return [None]
            res = []
            for i in range(len(nums)):
                for l in generate(nums[:i]):
                    for r in generate(nums[i + 1:]):
                        root = TreeNode(nums[i])
                        root.left = l
                        root.right = r
                        res.append(root)
            return res

        return generate(nums)
