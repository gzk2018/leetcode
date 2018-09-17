# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        self.res = []

        def inorder(node):
            if node is None:
                self.res.append('null')
                return
            self.res.append(node.val)
            inorder(node.left)
            inorder(node.right)

        inorder(root)
        return str(self.res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        res = iter(eval(data))

        # 如果用中序遍历的话，如果第一个数是‘null’，就直接退出程序了
        def inorder():
            val = next(res)
            if val == 'null':
                return
            else:
                root = TreeNode(val)
                left = inorder()
                right = inorder()
                root.left = left
                root.right = right
                return root

        root = inorder()
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))