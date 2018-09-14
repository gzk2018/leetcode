class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:return s
        n = len(s)
        index = 0
        # 相当于strip
        while index < n and s[index] == ' ':index += 1
        while n > 1 and s[n - 1] == ' ': n -= 1
        start = index
        res = []
        while index < n:
            if s[index] == ' ':
                res.append(s[start:index])
                # 连续空格
                while s[index] == ' ':index += 1
                start = index
            else:
                index += 1
        if start < index: res.append(s[start:index])
        return ' '.join(res[::-1])