# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        def has_k(head):
            i = 1
            while head.next:
                head = head.next
                i += 1
                if i >= k:
                    return True
            return False

        if k == 1: return head
        dummy = ListNode(None)
        dummy.next = head
        pre = dummy
        cur = head
        before = dummy
        while cur:
            if has_k(cur):
                temp = cur
                pre = cur
                cur = cur.next
                for i in range(k - 1):
                    after = cur.next
                    cur.next = pre
                    pre = cur
                    cur = after
                before.next = pre
                temp.next = cur
                before = temp
            else:
                break
        return dummy.next








