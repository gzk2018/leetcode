class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """

        def f(s):
            if len(s) == 1 or set(s) == {'0'}:
                return s
            else:
                return s.lstrip('0')

        v1, v2 = list(map(f, version1.split('.'))), list(map(f, version2.split('.')))

        index = 0
        while index < min(len(v1), len(v2)):
            var1, var2 = int(v1[index]), int(v2[index])
            if var1 < var2:
                return -1
            elif var1 > var2:
                return 1
            index += 1

        if not v1:
            while index < len(v2):
                if v2[index] > '0':
                    return -1
                index += 1
            return 0
        elif not v2:
            while index < len(v1):
                if v1[index] > '0':
                    return 1
                index += 1
            return 0
        else:
            return 0

s = Solution()
s.compareVersion("1","1.1")