class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        def common(a, b):
            res = ""
            for i in range(min(len(a), len(b))):
                if a[i] == b[i]:
                    res += a[i]
                else:
                    break
            return res

        if not strs: return ""
        res = strs[0]
        for i in range(1, len(strs)):
            if not res: return ""
            res = common(res, strs[i])
        return res