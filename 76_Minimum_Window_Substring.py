class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) < len(t): return ""
        dic = {}
        for char in t:
            dic[char] = dic.get(char, 0) + 1
        begin = start = 0
        remain = len(t)
        length = len(s)
        isDone = False
        for i in range(len(s)):
            if dic.get(s[i], 0) > 0:
                remain -= 1
            dic[s[i]] = dic.get(s[i], 0) - 1

            if remain == 0:
                if not isDone:
                    begin = 0
                    length = i
                    isDone = True
                while dic[s[start]] < 0:
                    dic[s[start]] += 1
                    start += 1

                if i - start < length:
                    begin = start
                    length = i - start
        return s[begin:begin + length + 1] if isDone else ""