class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        letter = ''
        for i in range(26):
            letter += chr(ord('A') + i)
        res = ''
        while n > 0:
            n -= 1
            res += letter[n%26]
            n = n // 26
        return res[::-1]