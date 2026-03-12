class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        n = 0 
        lenght_ = len(arr) - 1
        for left in range(lenght_ + 1):
            if left > lenght_ - n:
                break
            
            if arr[left] == 0:
                if left == lenght_ - n:
                    arr[lenght_] = 0
                    lenght_ -= 1
                    break
                n += 1
        
        last = lenght_ - n
        for i in range(last, -1, -1):
            if arr[i] == 0:
                arr[i + n] = 0
                n -= 1
                arr[i + n] = 0
            else:
                arr[i + n] = arr[i]