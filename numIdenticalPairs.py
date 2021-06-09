def numIdenticalPairs(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    ## keep a count of each num in a dictionary
    ## and then add it up 
    d = {}

    for num in nums:
        if num not in d:
            d[num] = 1
        else:
            d[num]+=1

    result=0
    for each in d:
        if d[each] > 1:
            result = result + d[each] * (d[each] -1)/2
    
    return int(result)

    

    

if __name__ == '__main__':
    nums1 = [1,2,3,1,1,3]
    nums2 = [1,1,1,1]
    nums3 = [1,2,3]

    print(numIdenticalPairs(nums1))
    print(numIdenticalPairs(nums2))
    print(numIdenticalPairs(nums3))

else:
    pass