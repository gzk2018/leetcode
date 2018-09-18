class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = ""
        ia, ib = len(a) - 1, len(b) - 1
        carry = 0
        while ia >= 0 or ib >= 0:
            digit = int(a[ia] if ia >= 0 else 0) + int(b[ib] if ib >= 0 else 0) + carry
            carry = digit // 2
            digit = digit % 2

            res += str(digit)
            ia -= 1
            ib -= 1
        if carry:
            res += '1'
        return res[::-1]