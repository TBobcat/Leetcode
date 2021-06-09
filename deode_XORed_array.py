class Solution(object):
    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        """
        i = 0
        res = [None]* (len(encoded)+1)
        res[0]=first
        
        while i < len(encoded):
            res[i+1] = encoded[i] ^ res[i]
            #print(res)
            i+=1
                
        return res