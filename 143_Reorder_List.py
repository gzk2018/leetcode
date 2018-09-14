# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:return
        # 找中点
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        even = slow
        odd = head

        # reverse even link
        # dummy = ListNode(None)
        # dummy.next = even
        pre, cur = None, even
        while cur:
            after = cur.next
            cur.next = pre
            pre = cur
            cur = after
        # even.next = None

        # merge:
        # 在找中点的时候，中点前的node并没有指向空，而是指向他最后应该指向的node，
        # 所以while条件为cur2.next
        cur1, cur2 = odd, pre
        while cur2.next:
            after1, after2 = cur1.next, cur2.next
            cur1.next = cur2
            cur2.next = after1
            cur1, cur2 = after1, after2