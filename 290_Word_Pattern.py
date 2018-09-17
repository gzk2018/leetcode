class Solution:
    def wordPattern(self, pattern, strs):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        dic = {}
        dic2 = {}
        strs = strs.split()
        if len(pattern) != len(strs):
            return False
        for i in range(len(strs)):
            if pattern[i] not in dic:
                dic[pattern[i]] = strs[i]
            else:
                if dic[pattern[i]] != strs[i]:
                    return False

            if strs[i] not in dic2:
                dic2[strs[i]] = pattern[i]
            else:
                if dic2[strs[i]] != pattern[i]:
                    return False
        return True