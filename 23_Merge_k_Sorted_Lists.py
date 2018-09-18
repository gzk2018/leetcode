from queue import PriorityQueue as pq
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        stack = pq()
        for node in lists:
            if node:
                stack.put((node.val,node))
        dummy = ListNode(None)
        cur = dummy
        while stack.qsize() > 0:
            val, node = stack.get()
            cur.next = node
            cur = cur.next
            if node.next:
                stack.put((node.next.val, node.next))
        return dummy.next