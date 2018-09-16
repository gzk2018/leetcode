class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 将所有数抑或，得到的结果为最终结果的异或值
        xor = nums[0]
        for i in range(1, len(nums)):
            xor = xor^nums[i]
        # 结果的第i位为1，则说明在这一位上两个数的值不一样
        # mask找出在哪一位上两个数的值不一样
        mask = 1
        while mask&xor == 0:
            mask = mask << 1
        # 按照不一样的这一位，将所有数字分为两拨分别抑或
        # 最终的值就是两个唯一出现的数值
        first = second = 0
        for num in nums:
            if num & mask:
                first ^= num
            else:
                second ^= num
        return [first, second]