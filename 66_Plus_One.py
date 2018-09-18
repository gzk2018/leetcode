class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        n = len(digits)
        digits[-1] += 1
        carry = 0
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += carry
            carry = digits[i] // 10
            digits[i] = digits[i] % 10
            if not carry:return digits
        return digits if not carry else [1] + digits