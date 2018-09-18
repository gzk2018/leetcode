class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words: return []
        res = []
        wordlen = len(words[0])
        n = len(s)
        wordbank = {}
        for word in words:
            wordbank[word] = wordbank.get(word, 0) + 1

        for i in range(wordlen):
            left = i
            dic = {}
            for j in range(i, n - wordlen + 1, wordlen):
                right = j + wordlen
                substr = s[j:j + wordlen]
                if substr in wordbank:
                    dic[substr] = dic.get(substr, 0) + 1
                    while dic[substr] > wordbank[substr]:
                        dic[s[left:left + wordlen]] -= 1
                        left += wordlen
                    if right - left == wordlen * len(words):
                        res.append(left)
                        dic[s[left:left + wordlen]] -= 1
                        left += wordlen
                else:
                    dic = {}
                    left = right
        return res




