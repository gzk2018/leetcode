import random


class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}
        self.data = []

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        dic, data = self.dic, self.data
        if val in dic:
            return False
        else:
            n = len(data)
            self.data.append(val)
            dic[val] = n

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        dic, data = self.dic, self.data
        if val not in dic:
            return False
        else:
            index = dic[val]
            n = len(data) - 1
            data[index], data[n] = data[n], data[index]
            dic[data[index]] = index
            data.pop()
            del dic[val]
            return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        data = self.data
        index = random.randint(0, len(data) - 1)
        return data[index]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()