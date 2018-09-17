class Solution:
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        n = len(secret)
        bull = 0
        for i in range(n):
            if secret[i] == guess[i]:
                bull += 1

        dic1, dic2 = {}, {}
        for i in range(n):
            dic1[secret[i]] = dic1.get(secret[i], 0) + 1
            dic2[guess[i]] = dic2.get(guess[i], 0) + 1
        cow = 0
        for key, value in dic1.items():
            if key in dic2:
                cow += min(value, dic2[key])
        cow -= bull
        return str(bull) + 'A' + str(cow) + 'B'