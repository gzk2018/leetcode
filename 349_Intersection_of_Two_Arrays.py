class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        s1, s2 = set(), set()
        for i in nums1:
            s1.add(i)
        for i in nums2:
            s2.add(i)
        return list(s1 & s2)