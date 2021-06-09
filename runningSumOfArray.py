def runningSum(nums):
    """
    :type nums: List[int]
    :rtype:
    """ 
    result=list(range(len(nums)))
    #print(result)
    for i,num in enumerate(nums):
        if i == 0:
            result[i] = nums[i]
        else:
            result[i] = result[i-1] + num
    return result




if __name__ == '__main__':
    nums1 = [1,2,3,4]
    nums2 = [1,1,1,1,1]
    nums3 = [3,1,2,10,1]

    print(runningSum(nums1))
    print(runningSum(nums2))
    print(runningSum(nums3))

else:
    pass