class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        n=len(code)
        res=[0]*n
        extended=code+code

        if k==0:
            return res
        for i in range(n):
            if k>0:
                res[i]=sum(extended[i+1:i+k+1])
            else:
                res[i]=sum(extended[i+n+k:i+n])

        return res