class Solution(object):
    def stoneGameVII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        
        length = len(stones)
        
        ## construct the n x n matrix and prefix sum list
        dp = [[0] * length for _ in range(length)]
        
        ## had to construct prefix sum list cause sum(list_slicing) runtime exceeded
        p_sum = [0] + stones[:]
        
        for i in range(1, len(p_sum)):
		    p_sum[i] += p_sum[i-1]
        
        for i in range(length-1, -1, -1):
            for j in range(i+1, length):
                dp[i][j] = max (
                                   p_sum[j+1] - p_sum[i + 1] - dp[i+1][j],
                                   p_sum[j] - p_sum[i] - dp[i][j-1]
                    
                                )
        
                
        return dp[0][length-1]