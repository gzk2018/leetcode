# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(None)
        dummy.next = head
        pre, cur = dummy, head
        while cur:
            if cur.next and cur.next.val == cur.val:
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
                cur = cur.next
                pre.next = cur
            else:
                pre = cur
                cur = cur.next
        return dummy.next