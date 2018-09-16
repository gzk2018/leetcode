class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t): return False
        dicS = {}
        dicT = {}
        for i in range(len(s)):
            if s[i] not in dicS:
                dicS[s[i]] = t[i]
            else:
                if dicS[s[i]] != t[i]:
                    return False

            if t[i] not in dicT:
                dicT[t[i]] = s[i]
            else:
                if dicT[t[i]] != s[i]:
                    return False
        return True
