class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):return False
        dicS = {}
        dicT = {}
        for i in range(len(s)):
            dicS[s[i]] = dicS.get(s[i], 0) + 1
        for i in range(len(t)):
            dicT[t[i]] = dicT.get(t[i], 0) + 1
        return dicS == dicT