class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        strs = {}
        for ch in magazine:
            if ch in strs:
                strs[ch] += 1
            else:
                strs[ch] = 1
        
        for ch in ransomNote:
            if ch not in strs or strs[ch] == 0:
                return False
            strs[ch] -= 1
        
        return True