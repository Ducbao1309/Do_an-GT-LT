class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        consumed_bottles = 0

        while numBottles >= numExchange:
            consumed_bottles += numExchange
            numBottles -= numExchange
            numBottles += 1

        return consumed_bottles + numBottles