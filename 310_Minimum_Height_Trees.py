class Solution:
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1: return [0]
        dic = {}
        for i, j in edges:
            if i not in dic:
                dic[i] = []
            if j not in dic:
                dic[j] = []
            dic[i].append(j)
            dic[j].append(i)

        while len(dic) > 2:
            delete = []
            for key in dic.keys():
                if len(dic[key]) == 1:
                    delete.append(key)
            for d in delete:
                # 被删除的结点只有一个邻结点
                # 可以直接由dic[d][0]找出相邻结点是什么
                dic[dic[d][0]].remove(d)
                del dic[d]
            # for key in dic.keys():
            #     for d in delete:
            #         if d in dic[key]:
            #             dic[key].remove(d)
        return list(dic.keys())