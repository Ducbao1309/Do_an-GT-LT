class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        count = 0
        num = {}
        for i in nums3:
            for j in nums4:
                s = i + j
                if s in num:
                    num[s] += 1
                else:
                    num[s] = 1
        
        for i in nums1:
            for j in nums2:
                target = -(i + j)
                if target in num:
                    count += num[target]
            
        return count