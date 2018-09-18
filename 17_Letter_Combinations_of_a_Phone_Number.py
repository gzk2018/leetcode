class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits: return []
        letter_dict = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
                       '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}

        def comb(digits):
            if len(digits) == 1:
                return letter_dict[digits]
            ret = []
            for pre in letter_dict[digits[0]]:
                for aft in comb(digits[1:]):
                    ret.append(pre + aft)
            return ret

        return comb(digits)
