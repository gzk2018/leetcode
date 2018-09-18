# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:return head
        n = 1
        cur = head
        while cur.next:
            n += 1
            cur = cur.next
        tail = cur
        target = n - k % n
        index, cur = 1, head
        res = None
        while cur:
            if index == target and cur.next is not None:
                res = cur.next
                cur.next = None
                tail.next = head
                break
            cur = cur.next
            index += 1
        return res if res else head