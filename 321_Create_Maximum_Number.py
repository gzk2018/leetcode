class Solution:
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """

        # 在一个数组里挑k个保持原有顺序条件下最大的数
        def createMax(nums, k):
            stack = []
            index, n = 0, len(nums)
            while index < n:
                remain = n - index
                while stack and stack[-1] < nums[index] and remain > k:
                    stack.pop()
                    # stack 出栈，就需要新元素入栈，最后满足长度为k
                    k += 1
                if k > 0:
                    stack.append(nums[index])
                    k -= 1
                index += 1
            return stack

        def merge(nums1, nums2):
            res = []
            # bad case:[6,7], [6,0,4]
            # merge时不知道第二位哪个大，如果从nums2选择第一个数的话
            # 第二个数最大为6，结果是66704

            # index1 = index2 = 0
            # while index1 < len(nums1) and index2 < len(nums1):
            #     if nums1[index1] > nums2[index2]:
            #         res.append(nums1[index1])
            #         index1 += 1
            #     else:
            #         res.append(nums2[index2])
            #         index2 += 1
            # if index1 < len(nums1):
            #     res += nums1[index1:]
            # elif index2 < len(nums2)
            #     res += nums2[index2:]
            # return res

            while nums1 or nums2:
                # 比较的不是当前位置哪个数字大，而是合在一起哪个看起来更大
                if nums1 > nums2:
                    res.append(nums1[0])
                    nums1 = nums1[1:]
                else:
                    res.append(nums2[0])
                    nums2 = nums2[1:]
            return res

        res = [0] * k
        for i in range(k + 1):
            j = k - i
            if i <= len(nums1) and j <= len(nums2):
                array1 = createMax(nums1, i)
                array2 = createMax(nums2, j)
                res = max(res, merge(array1, array2))
        return res


