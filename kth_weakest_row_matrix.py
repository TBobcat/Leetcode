class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        d = {}
        
        #O(n *m), m is length of each list, aka column number
        for index, row in enumerate(mat):
            solds = sum(row)
            d[index] = solds
         
        # sort by dict values ascending only, lambda makes it sort by x[1]
        # first, and then x[0]
        # returns a list of key value pairs
        # since it's builtin sort, assume O(nlogn)
        sorted_lst = sorted(d.items(), key=lambda x: (x[1], x[0]))
        
        return map(lambda x: x[0], sorted_lst[:k])
            
        # space complexity: is O(n) for d, + O(n) for sorted_lst, 
        # which is O(2n), so O(n)