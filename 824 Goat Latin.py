class Solution(object):
    def toGoatLatin(self, sentence):
        """
        :type sentence: str
        :rtype: str
        """
        temp = []
        ans = " " 
        i = 1
        vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        for word in sentence.split(" "):
            if word[0] in vowel:
                word = word + "ma"
            else:
                word = word[1:] + word[0] + "ma"
            word = word + "a"*i
            i = i + 1
            temp.append(word)
		# Joins all the list elements.
        return ans.join(temp)
