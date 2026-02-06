class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        length = len(flowerbed)

        for i in range(length):
            if flowerbed[i] == 0:
                is_left_empty = (i == 0) or (flowerbed[i - 1] == 0)
                is_right_empty = (i == length - 1) or (flowerbed[i + 1] == 0)

                if is_left_empty and is_right_empty:
                    flowerbed[i] = 1
                    n -= 1

                    if n == 0:
                        return True
        
        return n <= 0