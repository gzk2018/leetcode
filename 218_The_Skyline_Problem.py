import heapq as hp


class Solution:
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        height = []
        for size in buildings:
            # 为了区分左右，左边高度为负，右边为正
            height.append([size[0], -size[2]])
            height.append([size[1], size[2]])
        # 按从左到右的顺序排号
        height.sort()

        # stack里面储存高度
        stack = []
        hp.heapify(stack)
        res = []

        # 地平线的高度
        # 需要加入0，因为两个楼房分开的话，分开那段高度为0
        pre_height = 0
        hp.heappush(stack, 0)

        # 每一个天际线的点只可能是楼房的左边或者是右边
        for h in height:
            # 如果是左边的话，说明这个高度在当前范围内
            # 由于堆是最小堆，所以要把高度取负变成最大堆
            if h[1] < 0:
                stack.append(h[1])
            # 如果在右边，说明当前高度已结束，要出栈
            else:
                stack.remove(-h[1])
            hp.heapify(stack)

            cur_height = stack[0]
            if pre_height != cur_height:
                res.append([h[0], -cur_height])
                pre_height = cur_height
        return res