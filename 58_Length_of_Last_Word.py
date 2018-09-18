class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        index, count = n - 1, 0

        while index >= 0:
            if s[index] == ' ':
                index -= 1
            else:
                while index >= 0 and s[index] != ' ':
                    index -= 1
                    count += 1
                break
        return count