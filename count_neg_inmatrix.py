class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        print(self.count_neg([1,2,-1]))
        return sum([self.count_neg(lst) for lst in grid])

    def count_neg(self, lst):    
        start = 0
        end = len(lst)-1
        
        # find index of fist negative number at start
        while end >= start:
            mid = (start + end)//2
            
            if lst[mid] >= 0:
                start = mid+1
            else:
                end = mid-1
        
        return len(lst)-start