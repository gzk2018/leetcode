# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dummy = ListNode(None)
        dummy.next = head
        cur = head
        pointer = pre = dummy
        while cur:
            if cur.val < x:
                a = pre.next
                after = cur.next
                pre.next = cur.next
                temp = pointer.next
                pointer.next = cur
                cur.next = temp
                pointer = cur
                cur = after
                # 其他步骤和数组一样，加上这个判断条件
                if pre.next == a:
                    pre = pre.next
            else:
                pre = cur
                cur = cur.next
        return dummy.next