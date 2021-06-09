## can import module in leetcode like
## import numpy as np

def shuffle(nums, n):
    """
    :type nums: List[int]
    :type n: int
    :rtype: List[int]
    """
    res = list(range(2*n))
    first_half = nums[:n]
    second_half = nums[n:]
    
    print(first_half, second_half)

    i = 0
    while i <= 2*n-1:
        if i % 2 == 0:
            res[i] = first_half[0]
            first_half.pop(0)
        else:
            res[i] = second_half[0]
            second_half.pop(0)
    
        i+=1
    return res


if __name__ == '__main__':
    nums1 = [2,5,1,3,4,7]
    n1 = 3
 
    nums2 = [1,2,3,4,4,3,2,1]
    n2 = 4

    nums3 = [1,1,2,2]
    n3 = 2

    print(shuffle(nums1, n1))
    print(shuffle(nums2, n2))
    print(shuffle(nums3, n3))

else:
    pass