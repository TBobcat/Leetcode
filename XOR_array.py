class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        nums = [None]*n
        
        for i,num in enumerate(nums):
            ## modify the list item, not the num
            nums[i] = start + 2*i
            
        return reduce(lambda x,y: x ^ y, nums)