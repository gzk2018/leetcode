# 用trie树做查找
class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.end = False


class TrieTree(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.end = True


class Solution:
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        trie = TrieTree()
        root = trie.root
        for word in words:
            trie.insert(word)

        res = []
        m, n = len(board), len(board[0])

        def dfs(x, y, path, node):
            if node.end:
                node.end = False
                res.append(path)

            sur = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
            temp = board[x][y]
            board[x][y] = '.'
            for i, j in sur:
                if 0 <= i < m and 0 <= j < n and board[i][j] in node.children:
                    dfs(i, j, path + board[i][j], node.children[board[i][j]])
            board[x][y] = temp

        for i in range(m):
            for j in range(n):
                if board[i][j] in root.children:
                    dfs(i, j, board[i][j], root.children[board[i][j]])
        return res



