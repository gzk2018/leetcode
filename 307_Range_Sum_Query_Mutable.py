class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        nums = [0] + nums
        n = len(nums)
        tree = [0] * n
        for i in range(1, n):
            j = i
            # & 优先级比 - 低
            # tree 的第i个元素为数组的第[i-2^k+1] 一直加到第i个
            # i&(-i)的意义为i的二进制连续的0前面加上1后，代表的十进制数
            lower_bound = i - ((i) & (-i))
            while i > lower_bound:
                tree[j] += nums[i]
                i -= 1
        self.tree = tree
        self.nums = nums
        print(tree)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        tree = self.tree
        nums = self.nums
        i += 1
        change = val - nums[i]
        self.nums[i] = val
        while i < len(nums):
            tree[i] += change
            i += i & (-i)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        tree = self.tree
        j += 1
        ans = 0
        while j > 0:
            ans += tree[j]
            j -= j & (-j)

        while i > 0:
            ans -= tree[i]
            i -= i & (-i)
        return ans

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)