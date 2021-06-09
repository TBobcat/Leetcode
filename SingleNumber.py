def singleNumber(nums):

    """
    :type nums: List[int]
    :rtype: int
    """
    d = {}
    for num in nums:
         if num in d:
             d[num] = d[num] + 1
         else:
             d[num] = 1

    # print(d)
    # print(list(d.values()).index(1))
    # print(list(d.keys()))
    return list(d.keys())[list(d.values()).index(1)]
    





if __name__ == '__main__':
    nums1=[2,2,1]
    nums2=[4,1,2,1,2]

    nums3=[1]

    print(singleNumber(nums1))
    print(singleNumber(nums2))
    print(singleNumber(nums3))

else:
    pass