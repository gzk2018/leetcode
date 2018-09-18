class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        Is_valid = True
        stack = []
        char_dict = {'[': ']', '(': ')', '{': '}'}
        for char in s:
            if char in char_dict.keys():
                stack.append(char)
            if char in char_dict.values():
                if not stack or char_dict[stack.pop()] != char:
                    Is_valid = False
                    break
        if stack:
            Is_valid = False

        return Is_valid
