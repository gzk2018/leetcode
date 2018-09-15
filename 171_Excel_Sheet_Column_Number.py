class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        for i in range(26):
            dic[chr(ord('A')+i)] = i+1
        res, base = 0, 1
        for i in range(len(s)-1,-1,-1):
            res += base*dic[s[i]]
            base *= 26
        return res