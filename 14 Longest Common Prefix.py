class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        result = ""

        for i in range(len(strs[0])):
            current_char = strs[0][i]

            for s in strs:
                if i >= len(s) or s[i] != current_char:
                    return result

            result += current_char

        return result

        

        
        
