class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost.sort()
        total = 0
        n = len(cost)

        for i in range(n):
            if (n - i) % 3 != 0:
                total += cost[i]

        return total