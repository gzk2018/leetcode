# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:return head
        dummy = ListNode(None)
        dummy.next = head
        pre = dummy
        slow = fast = head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        pre.next = None
        root = TreeNode(slow.val)
        if slow is head:return root
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)
        return root