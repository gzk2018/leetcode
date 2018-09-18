class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for char in strs:
            key = ''.join(sorted(char))
            print(key)
            if key not in dic:
                dic[key] = []
            dic[key].append(char)
        ret = []
        for value in dic.values():
            ret.append(value)
        return ret