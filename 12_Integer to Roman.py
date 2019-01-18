class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # d4d3d2d1
        digit = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]  # 所有的特殊表达
        number = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman = ""
        for i in range(len(digit)):
            if num < number[i]:
                continue
            while num >= number[i]:
                roman += digit[i]
                num -= number[i]

        return roman
