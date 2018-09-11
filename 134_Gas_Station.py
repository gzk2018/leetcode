class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost): return -1
        n = len(gas)
        start = index = 0
        amount = gas[0]
        while index < n - 1:
            # the remaining amount if arriving next station
            amount -= cost[index]
            # index should increase first cuz cost[i] means
            # the cost of gas to travel from station i to its next station (i+1)
            index += 1
            if amount < 0:
                start = index
                amount = gas[index]
            else:
                amount += gas[index]
        return start
