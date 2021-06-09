def binary_search(nums, num):
    # iterate calculation of mid to compare to num
    # and see if it's equal

    left_i = 0
    right_i = len(nums)-1

    while(left_i <= right_i):
        mid = int(left_i + (right_i-left_i)/2)

        if nums[mid] == num:
            return mid
        elif nums[mid] > num:
            right_i = mid
        else:
            left_i = mid
    
    return mid 
  

if __name__ == '__main__':

    lst1 = [5,10,25,30,32,43,51]

    lst2 = [5,10,25,30,32,43]

    print(binary_search(lst1, 32))
    print(binary_search(lst2, 30))

else:
    pass

