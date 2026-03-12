class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashmap = {}
        for i in nums:
            if i in hashmap.keys():
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        sum = 0
        for k, v in hashmap.items():
            if v == 1: sum += k
        return sum