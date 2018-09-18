class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = []
            dic[s[i]].append(i)
        res = len(s)
        for key, value in dic.items():
            if len(value) == 1:
                res = min(res, value[0])
        return res if res != len(s) else -1
