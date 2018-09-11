# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node: return
        root, visited, level = UndirectedGraphNode(node.label), {}, [node]
        visited[node] = root
        while level:
            nextlevel = []
            for node in level:
                for adj in node.neighbors:
                    if adj not in visited:
                        newnode = UndirectedGraphNode(adj.label)
                        visited[adj] = newnode
                        nextlevel.append(adj)
                    # visited[node].neighbors.append(newnode)
                    visited[node].neighbors.append(visited[adj])
            level = nextlevel
        return root


