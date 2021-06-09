from typing import List

# below uses two loops which gets to O(n^2) run time
# if use a hash map it will be O(n)+O(1) which is O(n)
def twoSum(nums: List[int], target: int) -> List[int]:
    x,y = 0,1
    for i,num in enumerate(nums, start=0):
        x = i
        y = x+1
        print('index of x is',i, 'number', num)
        for j,num2 in enumerate(nums[i+1:]):
            print('index of y is', y)
            if target - num2 == num:
                y = y+j
                return [x,y]
        



if __name__ == '__main__':
    nums1 = [2,7,11,15]
    target1 = 9
    nums2 = [3,2,4]
    target2 = 6
    nums3 = [3,3]
    target3 = 6
    nums4=[3,2,3]
    target4=6

    nums5=[2,5,5,11]
    target5=10

    nums6=[0,4,3,0]
    target6=0

    print(twoSum(nums1, target1))
    print(twoSum(nums2, target2))
    print(twoSum(nums3, target3))
    print(twoSum(nums4, target4))
    print(twoSum(nums5, target5))

    print(twoSum(nums6, target6))

else:
    pass

