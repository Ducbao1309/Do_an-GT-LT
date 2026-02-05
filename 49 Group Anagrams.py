class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram = {}

        for i in strs:
            arr = tuple(sorted(i))
            if arr not in anagram:
                anagram[arr] = [i]
            else:
                anagram[arr].append(i)
            
        return list(anagram.values())