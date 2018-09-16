# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        index = 0
        slow = fast = head
        while slow and fast and fast.next:
            index += 1
            slow = slow.next
            fast = fast.next.next
        mid = slow
        pre, cur = None, slow
        while cur:
            after = cur.next
            cur.next = pre
            pre = cur
            cur = after

        cur = head
        while pre and cur:
            if pre.val != cur.val:
                return False
            pre = pre.next
            cur = cur.next
        return True