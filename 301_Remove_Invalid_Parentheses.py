class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        def isvalid(s):
            count = 0
            for i in range(len(s)):
                if s[i] == '(':
                    count += 1
                elif s[i] == ')':
                    count -= 1
                if count < 0:
                    return False
            return count == 0

        if isvalid(s): return [s]

        #bfs 暴搜
        res = set()
        level = set([s])
        while level:
            nextlevel = set()
            for strs in level:
                for i in range(len(strs)):
                    temp = strs[:i] + strs[i + 1:]
                    if isvalid(temp):
                        res.add(temp)
                    nextlevel.add(temp)
            if res: return list(res)
            if not nextlevel: return [""]
            level = nextlevel




