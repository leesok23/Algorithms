class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if cost == []:
            return 0
        elif len(cost) == 1:
            return cost[0]
        
        cost0, cost1 = cost[0], cost[1]
        for i in range(2, len(cost)):
            cost0, cost1 = cost1, cost[i] + min(cost0, cost1)
        
        return min(cost0, cost1)
