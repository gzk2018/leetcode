class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [1 for i in range(n)]

        # 从第二项开始，累积乘积
        # 第二项为第一项乘积
        # 第三项为第一二项乘积
        # 第四项为第一二三项乘积
        for i in range(1, n):
            res[i] = nums[i - 1] * res[i - 1]

        # 最后一项已经是之前所有的乘积，不用补充
        # 从倒数第二项开始补充
        coeff = nums[-1]
        for i in range(n - 2, -1, -1):
            res[i] = res[i] * coeff
            coeff *= nums[i]
        return res