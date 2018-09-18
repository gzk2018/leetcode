# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        index = 1
        dummy = ListNode(0)
        dummy.next = head
        pre, cur = dummy, head
        while cur:
            if index == m:
                before = pre
                tail = cur
                temp = ListNode(None)
                temp.next = cur
                pre = temp
                while index <= n:
                    after = cur.next
                    cur.next = pre
                    pre = cur
                    cur = after
                    index += 1
                before.next = pre
                tail.next = after
            else:
                pre = cur
                cur = cur.next
                index += 1
        return dummy.next