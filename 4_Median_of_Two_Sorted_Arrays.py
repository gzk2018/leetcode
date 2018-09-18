class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        def findk(nums1, nums2, k):
            if not nums1:
                return nums2[k]
            elif not nums2:
                return nums1[k]
            n1, n2 = len(nums1), len(nums2)
            index1, index2 = n1 // 2, n2 // 2
            mid1, mid2 = nums1[index1], nums2[index2]

            if index1 + index2 >= k:
                if mid1 >= mid2:
                    return findk(nums1[:index1], nums2, k)
                else:
                    return findk(nums1, nums2[:index2], k)
            else:
                if mid1 >= mid2:
                    return findk(nums1, nums2[index2 + 1:], k - index2 - 1)
                else:
                    return findk(nums1[index1 + 1:], nums2, k - index1 - 1)

        n1, n2 = len(nums1), len(nums2)
        if (n1 + n2) % 2 == 1:
            return findk(nums1, nums2, (n1 + n2) // 2)
        else:
            return (findk(nums1, nums2, (n1 + n2) // 2) + findk(nums1, nums2, (n1 + n2) // 2 - 1)) / 2
