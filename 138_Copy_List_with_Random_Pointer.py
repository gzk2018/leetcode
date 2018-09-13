# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head: return
        visited = {}
        cur = head
        while cur:
            # 后面的node可能已经存在了，因为被random指向
            if cur not in visited:
                newnode = RandomListNode(cur.label)
                visited[cur] = newnode
            else:
                newnode = visited[cur]

            if cur.next not in visited:
                visited[cur.next] = RandomListNode(cur.next.label) if cur.next else None
            newnode.next = visited[cur.next]

            # 判断random是否存在
            if cur.random:
                if cur.random not in visited:
                    visited[cur.random] = RandomListNode(cur.random.label)
                newnode.random = visited[cur.random]
            cur = cur.next
        return visited[head]
