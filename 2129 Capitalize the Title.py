from turtle import title

class Solution(object): 
    def capitalizeTitle(self, title): 
        """"
        :type title: str
        :rtype: str
        """
        result = []
        for word in title.split():
            if len(word) < 3:
                result.append(word.lower())
            else:
                result.append(word.title())        
        return " ".join(result)