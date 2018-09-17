class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        res = []

        # mul_res储存上一步计算出来的结果，为下一个乘法做准备
        def dfs(index, path, mul_res, s):
            if index == len(num):
                if s == target:
                    res.append(path)
                return

            if num[index] == '0':
                dfs(index + 1, path + '+0', 0, s)
                dfs(index + 1, path + '-0', 0, s)
                dfs(index + 1, path + '*0', 0, s - mul_res)
            else:
                for i in range(index, len(num)):
                    digits = int(num[index:i + 1])
                    dfs(i + 1, path + '+' + num[index:i + 1], digits, s + digits)
                    dfs(i + 1, path + '-' + num[index:i + 1], -digits, s - digits)
                    # 乘法的时候相当于乘上上一步的结果
                    dfs(i + 1, path + '*' + num[index:i + 1], mul_res * digits, s - mul_res + digits * mul_res)

        for i in range(len(num)):
            # 不管第一个数字是否为0都可以这样
            if i == 0:
                dfs(1, num[:1], int(num[:1]), int(num[:1]))
            # 第一个数字不为0的情况
            elif i > 0 and num[0] != '0':
                dfs(i + 1, num[:i + 1], int(num[:i + 1]), int(num[:i + 1]))
        return res




