class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 当成成环链表问题
        index = 0
        slow = nums[index]
        fast = nums[nums[index]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        head = nums[index]
        slow = nums[slow]
        while head != slow:
            slow = nums[slow]
            head = nums[head]
        return slow

