class Solution(object):
    def maxDistance(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        n = len(colors)
        result = 0

        for i in range(n):
            if colors[i] != colors[0]:
                result = max(result, i)
            if colors[i] != colors[n - 1]:
                result = max(result, n - 1 - i)
        
        return result