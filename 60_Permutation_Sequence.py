from math import factorial as f


class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        self.res = None

        def findk(nums, k, res):
            if not nums:
                self.res = res
                return

            base = f(len(nums) - 1)
            r = k // base
            q = k % base
            findk(nums[:r] + nums[r + 1:], q, res + nums[r])

        res = ""
        nums = []
        for i in range(n):
            nums.append(str(i + 1))
        findk(nums, k - 1, res)
        return self.res