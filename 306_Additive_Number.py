class Solution:
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        self.res = False
        if num == '0' * n and n >= 3: return True

        def dfs(index, path):
            if index == n or self.res:
                if len(path) >= 3:
                    self.res = True
                return

            if num[index] == '0':
                # 不能以0开头，如果path已经大于两个数字了，中间再遇到0直接返回
                if len(path) < 2:
                    dfs(index + 1, path + [0])
                else:
                    return
            else:
                if len(path) < 2:
                    for i in range(index, len(num)):
                        dfs(i + 1, path + [int(num[index:i + 1])])
                else:
                    for i in range(index, len(num)):
                        temp = int(num[index:i + 1])
                        if path[-1] + path[-2] == temp:
                            dfs(i + 1, path + [temp])

        dfs(0, [])
        return self.res
