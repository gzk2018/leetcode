class Solution(object):
    def diffWaysToCompute(self, inputs):
        """
        :type input: str
        :rtype: List[int]
        """
        operator = {
            '+': lambda x,y:x+y,
            '-': lambda x,y:x-y,
            '*': lambda x,y:x*y
        }
        if inputs.isdigit():
            return [int(inputs)]
        res = []
        # 简单的递归
        for i in range(len(inputs)):
            if inputs[i] in operator:
                for left in self.diffWaysToCompute(inputs[:i]):
                    for right in self.diffWaysToCompute(inputs[i+1:]):
                        res.append(operator[inputs[i]](left, right))
        return res