class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        start = 0
        res = 0
        dic = {}
        for i in range(len(s)):
            if s[i] in dic:
                start = max(dic[s[i]] + 1, start)
            res = max(res, i - start)
            dic[s[i]] = i
        return res + 1

