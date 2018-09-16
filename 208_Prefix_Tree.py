class TrieNode(object):
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.end = False


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode(None)

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        root = self.root
        cur = root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode(char)
            cur = cur.children[char]
        cur.end = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        root = self.root
        cur = root
        for char in word:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return cur.end

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        root = self.root
        cur = root
        for char in prefix:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)