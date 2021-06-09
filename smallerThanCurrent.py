def smallerNumbersThanCurrent(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    print(nums)

    d = {}
    result=[]

    # sorted keeps the original list and returns a new list
    for i,num in enumerate(sorted(nums)):
        ## this sets value only if key is not already existent
        ## returns None, or the value if it's set

        ## this algo means if the number is not repeated in a sorted
        ## list, the index is the count of numbers less than the number
        return_holder=d.setdefault(num,i)
    
    for num in nums:
        result.append(d[num])
    
    return result


if __name__ == '__main__':
    nums1 = [6,5,4,8]
    nums2 = [7,7,7,7]
    nums3 = [8,1,2,2,3]

    print(smallerNumbersThanCurrent(nums1))
    print(smallerNumbersThanCurrent(nums2))
    print(smallerNumbersThanCurrent(nums3))

else:
    pass