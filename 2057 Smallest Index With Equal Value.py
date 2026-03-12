class Solution(object):
    def smallestEqual(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for idx, n in enumerate(nums):
            if idx % 10 == n:
                return idx
        return -1