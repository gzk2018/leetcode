class str2(str):
    def __lt__(this, x):
        return (this + x) < (x + this)


class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = sorted(map(str, nums), key = str2, reverse = True)
        return ''.join(nums) if nums[0] != '0' else '0'
