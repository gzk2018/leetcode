class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        # 度
        degree = 1
        for i in preorder.split(','):
            # 每经过一个结点入度-1
            degree -= 1
            if degree < 0:
                return False
            if i.isdigit():
                # 如果不是空结点，出度加2
                degree += 2

        return degree == 0