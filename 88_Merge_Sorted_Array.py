class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        cur = m + n - 1
        n1, n2 = m - 1, n - 1
        while n1 >= 0 or n2 >= 0:
            if n1 >= 0 and (n2 < 0 or nums1[n1] > nums2[n2]):
                nums1[cur] = nums1[n1]
                cur -= 1
                n1 -= 1
            else:
                nums1[cur] = nums2[n2]
                cur -= 1
                n2 -= 1
