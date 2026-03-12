class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        for i in range(len(paths)):
            candidate = paths[i][1]
            good = True
            
            for j in range(len(paths)):
                if paths[j][0] == candidate:
                    good = False
                    break
                
            if good:
                return candidate
            
        return ""