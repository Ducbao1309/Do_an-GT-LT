class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        a = set(nums1) - set(nums2)
        b = set(nums2) - set(nums1)
        li = [list(a),list(b)]
        return li