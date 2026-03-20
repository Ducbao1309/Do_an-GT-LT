class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = []
        
        for a in nums:
            pair = [-abs(a), a]
            temp.append(pair)

        best = max(temp)

        return best[1]