# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:return head
        dummy = ListNode(None)
        dummy.next = head
        pre, cur, after = dummy, head, head.next
        while cur and cur.next:
            pre.next = after
            cur.next = after.next
            after.next = cur
            pre = cur
            if cur and cur.next:
                cur = cur.next
                after = cur.next
            else:
                break
        return dummy.next