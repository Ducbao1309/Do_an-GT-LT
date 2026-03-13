class Solution(object):
    def countWords(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        count1 = {}
        count2 = {}
        
        for i in words1:
            count1[i] = count1.get(i, 0) + 1
        for i in words2:
            count2[i] = count2.get(i, 0) + 1

        result = 0
        for i in count1:
            if count1[i] == 1 and count2.get(i, 0) == 1:
                result += 1

        return result