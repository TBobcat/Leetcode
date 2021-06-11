class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = [None] * (n+1)
        
        for i in range(n+1):
            ans[i] = bin(i)[2:].count('1')
            
        return ans