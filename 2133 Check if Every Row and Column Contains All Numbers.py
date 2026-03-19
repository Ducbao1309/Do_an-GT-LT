class Solution(object):
    def checkValid(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        set_ = set(range(1,len(matrix)+1))
        return all(set_ == set(x) for x in matrix+list(zip(*matrix)))