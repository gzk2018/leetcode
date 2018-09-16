class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:return []
        first, second = nums[0], None
        count1 = count2 = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == first:
                count1 += 1
            elif nums[i] == second:
                count2 += 1
            else:
                if count1 and count2:
                    count1 -= 1
                    count2 -= 1
                elif count1:
                    # count1 -= 1 不用减一，相当于重新定义数字
                    second = nums[i]
                    count2 = 1
                else:
                    # count2 -= 1
                    first = nums[i]
                    count1 = 1
        c1 = c2 = 0
        for i in range(n):
            if nums[i] == first:
                c1 += 1
            if nums[i] == second:
                c2 += 1
        res = []
        if c1 > n // 3:
            res.append(first)
        if c2 > n // 3:
            res.append(second)
        return res