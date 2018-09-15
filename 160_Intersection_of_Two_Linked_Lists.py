# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        flagA = flagB = False
        curA, curB = headA, headB
        while curA and curB:
            if curA == curB:return curA
            curA = curA.next
            curB = curB.next
            if not curB and not flagB:
                curB = headA
                flagB = True
            if not curA and not flagA:
                curA = headB
                flagA = True
        return 