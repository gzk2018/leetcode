# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:return head
        dummy = ListNode(-2**31)
        dummy.next = head
        cur = head.next
        head.next = None
        while cur:
            after = cur.next
            pre, pt = dummy, dummy.next
            while pt and cur.val > pt.val:
                pre = pt
                pt = pt.next
            pre.next = cur
            cur.next = pt
            cur = after
        return dummy.next