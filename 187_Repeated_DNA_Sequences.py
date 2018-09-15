class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        dic = set()
        res = set()
        for i in range(len(s) - 9):
            gene = s[i:i+10]
            if gene in dic:
                res.add(gene)
            dic.add(gene)
        return list(res)