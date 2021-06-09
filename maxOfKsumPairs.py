##  Tow Pointer Soln that worked
# def maxOperations(nums, k):
#     """
#     :type nums: List[int]
#     :type k: int
#     :rtype: int
#     """
#     sorted_nums=sorted(nums)
#     i = 0
#     j = len(sorted_nums)-1
#     counter = 0
#     while i < j:
#         if sorted_nums[i] + sorted_nums[j] < k:
#             i+=1
#         elif sorted_nums[i] + sorted_nums[j] > k:
#             j-=1
#         else:
#             counter+=1
#             i+=1
#             j-=1


## hash map/ dictionary solution
def maxOperations(nums, k):
    d = {}
    res = 0
    for num in nums:
        if num in d.keys():
            d[num]+=1
        else:
            d[num] = 1
    
    print(d)
    for num in nums:
        complement = k - num

        if d[num]>0 :
            d[num] -= 1
            if d[complement] > 0:
                d[complement] -= 1
                res += 1


    print(d)    
    return res


if __name__ == '__main__':
    nums1 = [1,2,3,4]
    k1 = 5
    nums2 = [3,1,3,4,3] 
    k2 = 6

    #print(maxOperations(nums1, k1))
    print(maxOperations(nums2, k2))

else:
    pass