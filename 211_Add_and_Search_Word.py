class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 存放word到dic里时，可以把词长作为key，如果直接把word作为key没有意义
        self.dic = {}

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        dic = self.dic
        n = len(word)
        if n not in dic:
            dic[n] = set()
        dic[n].add(word)

    def issame(self, word1, word2):
        for i in range(len(word1)):
            if word2[i] != '.' and word1[i] != word2[i]:
                return False
        return True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        dic = self.dic
        n = len(word)
        if n not in dic:
            return False
        if word in dic[n]: return True
        for w in dic[n]:
            if self.issame(w, word):
                return True
        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)