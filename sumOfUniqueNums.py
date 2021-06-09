def sumOfUnique(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    d = {}

    for i,num in enumerate(nums):
        if num not in d:
            d[num] = 1
        else:
            d[num] += 1
    print(d)

    result=0
    for key in d:
        if d[key] == 1:
            result += key
    return result



if __name__ == '__main__':
    nums1 = [1,2,3,2]
    nums2 = [1,1,1,1]
    nums3 = [1,2,3,4,5]

    print(sumOfUnique(nums1))
    print(sumOfUnique(nums2))
    print(sumOfUnique(nums3))

else:
    pass