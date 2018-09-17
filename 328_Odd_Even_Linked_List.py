# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head
        odd = head
        even = head.next
        odd_head, even_head = odd, even
        head = even.next
        even.next = None
        index = 1
        while head:
            after = head.next
            head.next = None
            if index % 2 == 1:
                odd.next = head
                odd = odd.next
            else:
                even.next = head
                even = even.next
            head = after
            index += 1

        odd.next = even_head
        return odd_head


def disp(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    print(res)
    return res

a,b,c,d,e = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e
s = Solution()
res = s.oddEvenList(a)
disp(res)


