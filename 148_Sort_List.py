# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        def merge(a, b):
            cur1, cur2 = a, b
            cur = dummy = ListNode(None)
            while cur1 or cur2:
                if cur1 and (not cur2 or cur1.val < cur2.val):
                    cur.next = cur1
                    cur1 = cur1.next
                else:
                    cur.next = cur2
                    cur2 = cur2.next
                cur = cur.next
            return dummy.next

        def sort(head):
            if not head or not head.next: return head
            pre = dummy = ListNode(None)
            dummy.next = head
            slow = fast = head
            while slow and fast and fast.next:
                pre = slow
                slow = slow.next
                fast = fast.next.next
            pre.next = None
            a = sort(head)
            b = sort(slow)
            r = merge(a, b)
            return r

        return sort(head)

