from operator import add
class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        if rowIndex == 0:return row
        i = 1
        while i <= rowIndex:
            nextrow = list(map(add,row+[0],[0]+row))
            row = nextrow
            i += 1
        return row