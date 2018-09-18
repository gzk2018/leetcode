from collections import defaultdict as dd
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dic = dd(lambda:None)
        dummy = ListNode(None)
        dic[0] = dummy
        dummy.next = head
        cur = head
        i = 1
        dic[i] = cur
        while cur.next:
            cur = cur.next
            i += 1
            dic[i] = cur
        dic[i-n].next = dic[i-n+2]
        return dummy.next