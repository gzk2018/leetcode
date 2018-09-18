class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        prev = self.countAndSay(n - 1)
        res = ""
        index, n = 0, len(prev)
        while index < n:
            count = 1
            while index < n - 1 and prev[index] == prev[index + 1]:
                count += 1
                index += 1
            res += str(count) + prev[index]
            index += 1
        return res