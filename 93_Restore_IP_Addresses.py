class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []

        def dfs(path, index):
            if index == len(s) and len(path) == 4:
                res.append('.'.join(path))
                return
            elif len(path) == 4 or index == len(s):
                return

            if s[index] == '0':
                dfs(path + [s[index]], index + 1)
            else:
                for i in range(index, min(index + 3, len(s))):
                    if int(s[index:i + 1]) <= 255:
                        dfs(path + [s[index:i + 1]], i + 1)

        dfs([], 0)
        return res