class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        dic = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(a / b)
        }

        stack = []
        for char in tokens:
            if char not in dic:
                stack.append(int(char))
            else:
                b = stack.pop()
                a = stack.pop()
                res = dic[char](a, b)
                stack.append(res)
        return stack[-1]
