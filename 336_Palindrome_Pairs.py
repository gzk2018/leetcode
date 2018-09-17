class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        dic = {}
        for index, word in enumerate(words):
            dic[word] = index
        ret = []
        for word in words:
            if word == "":
                for s in words:
                    if s == s[::-1] and dic[word] != dic[s]:
                        ret.append([dic[word], dic[s]])
            else:
                for i in range(len(word)):
                    left,right = word[:i], word[i:]
                    left_re, right_re = left[::-1], right[::-1]
                    if left == left_re:
                        if right_re in dic and dic[right_re] != dic[word]:
                            ret.append([dic[right_re],dic[word]])
                    if right == right_re:
                        if left_re in dic and dic[word] != dic[left_re]:
                            ret.append([dic[word],dic[left_re]])
        return ret