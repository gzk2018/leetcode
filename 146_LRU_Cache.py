class BiLinkNode(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dic = {}
        self.capacity = capacity
        self.head = BiLinkNode('head', 'head')
        self.tail = BiLinkNode('tail', 'tail')
        self.head.next = self.tail
        self.tail.pre = self.head

    def deletenode(self, node):
        _pre, _next, dic = node.pre, node.next, self.dic
        del (dic[node.key])
        _pre.next = _next
        _next.pre = _pre

    def addnode(self, k, v):
        head, tail, dic = self.head, self.tail, self.dic
        if k in dic:
            self.deletenode(dic[k])

        newnode = BiLinkNode(k, v)
        after = head.next
        head.next = newnode
        newnode.pre = head
        newnode.next = after
        after.pre = newnode
        dic[k] = newnode

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        dic = self.dic
        if key in dic:
            res = dic[key].val
            self.deletenode(dic[key])
            self.addnode(key, res)
            return res
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        capacity = self.capacity
        tail = self.tail
        dic = self.dic
        self.addnode(key, value)
        if len(dic) > capacity:
            self.deletenode(tail.pre)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)