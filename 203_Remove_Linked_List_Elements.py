# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(None)
        dummy.next = head
        pre, cur = dummy, head
        while cur:
            if cur.val == val:
                after = cur.next
                pre.next = after
                cur = after
            else:
                pre = cur
                cur = cur.next
        return dummy.next