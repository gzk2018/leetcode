# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder:return
        root = TreeNode(postorder[-1])
        root_index = inorder.index(postorder[-1])
        inleft = inorder[:root_index]
        inright = inorder[root_index + 1:]
        len_left = len(inleft)
        postleft = postorder[:len_left]
        postright = postorder[len_left:-1]
        root.left = self.buildTree(inleft, postleft)
        root.right = self.buildTree(inright, postright)
        return root