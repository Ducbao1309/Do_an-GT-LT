class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        value=0
        original=x
        if x<0:
            return False
        while x>0:
           digit= x%10
           value=value*10+digit
           x=x//10
        if original==value:
            return True
        else :
            return False