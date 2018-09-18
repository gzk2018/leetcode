class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList = set(wordList)
        if endWord not in wordList: return 0
        beginWord = set([beginWord])
        endWord = set([endWord])
        res = 0
        letters = ""
        for i in range(26):
            letters += chr(ord('a') + i)

        while True:
            # 次数加1
            res += 1
            level = set()
            for word in beginWord:
                for i in range(len(word)):
                    for char in letters:
                        newword = word[:i] + char + word[i + 1:]
                        if newword in wordList:
                            level.add(newword)
            if not level:
                return 0
            beginWord = level
            if beginWord & endWord:
                return res + 1
            if len(beginWord) > len(endWord):
                beginWord, endWord = endWord, beginWord
            # 每次wordList只减去beginWord
            wordList -= beginWord
