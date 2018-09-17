class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # O(n)笨方法
        # count, n = 0, len(citations)
        # for i in range(n-1, -1, -1):
        #     if citations[i] >= (n - i):
        #         count += 1
        #     else:
        #         break
        # return count


        # O(logn)
        if not citations: return 0
        n = len(citations)
        # right = n的时候，查找数组内从左至右
        # 第一个满足citations[i] > n - i的位置i
        # 如果不存在就返回n
        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            if citations[mid] >= n - mid:
                right = mid
            else:
                left = mid + 1
        return n - right