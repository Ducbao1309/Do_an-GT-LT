import math

class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum = (n * (n + 1) // 2)
        pivot = int(math.sqrt(sum))
        return pivot if pivot * pivot == sum else -1