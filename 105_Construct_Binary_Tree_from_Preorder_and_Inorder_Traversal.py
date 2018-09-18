# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def recon(preo, ino):
            if not preo:return
            root = TreeNode(preo[0])
            root_index = ino.index(preo[0])
            in_left = ino[:root_index]
            in_right = ino[root_index + 1:]
            lenleft, lenright = len(in_left), len(in_right)
            pre_left = preo[1:lenleft + 1]
            # pre_right = preo[-lenright:] 这样写有问题，[-0:]表示取全部数组
            pre_right = preo[lenleft + 1:]
            root.left = recon(pre_left, in_left)
            root.right = recon(pre_right, in_right)
            return root
        return recon(preorder, inorder)