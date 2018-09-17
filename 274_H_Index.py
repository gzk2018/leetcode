class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:return 0
        citations.sort(reverse = True)
        n = len(citations)
        count = 0
        for i in range(n):
            # 第（i+1）篇文章，引用量大于等于i+1
            if citations[i] >= i + 1:
                count += 1
            else:
                break
        return count
