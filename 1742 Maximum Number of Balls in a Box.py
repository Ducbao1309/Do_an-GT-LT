from collections import defaultdict

class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        """
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        """
        def numberSum(number):
            sum1 = 0
            while number:
                sum1 += number%10
                number = number //10
            return sum1
        hashMap = defaultdict(int)
        
        for i in range(lowLimit, highLimit+1):
            hash_val = numberSum(i)
            hashMap[hash_val] += 1.
        values = hashMap.values()

        return max(values)