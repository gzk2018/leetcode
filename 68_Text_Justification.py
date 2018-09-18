class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        index, n = 0, len(words)
        res = []
        while index < n:
            wordlen = 0
            wordcount = 0
            wordbag = []
            while index < n and wordlen + wordcount + len(words[index]) <= maxWidth:
                wordbag.append(words[index])
                wordlen += len(words[index])
                wordcount += 1
                index += 1
            if index == n:
                line = ' '.join(wordbag) + ' ' * (maxWidth - wordlen - wordcount + 1)
                res += [line]
                break

            if wordcount == 1:
                line = wordbag[0] + ' ' * (maxWidth - wordlen)
            else:

                spacelen = maxWidth - wordlen
                line = ""
                if spacelen % (wordcount - 1) == 0:
                    for i in range(len(wordbag) - 1):
                        line += wordbag[i] + ' ' * (spacelen // (wordcount - 1))
                    line += wordbag[-1]
                else:
                    more_space = spacelen % (wordcount - 1)
                    for i in range(0, len(wordbag) - 1):
                        if more_space > 0:
                            line += wordbag[i] + ' ' * (spacelen // (wordcount - 1)) + ' '
                            more_space -= 1
                        else:
                            line += wordbag[i] + ' ' * (spacelen // (wordcount - 1))
                    line += wordbag[-1]
            res += [line]
        return res


