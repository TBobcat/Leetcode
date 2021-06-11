#!/usr/bin/env python3

print("hello, world!")

## using memoisation to store values as it goes top down
def can_sum(n, lst):
    memo = {}
    return helper(n, lst, memo)

def helper(n, lst, memo):
    if n in memo:
        return memo[n]
    if n == 0:
        return True
    if n < 0:
        return False

    for num in lst:
        remain = n - num
        if helper(remain, lst, memo) == True:
            memo[n] = True
            return True

    memo[n] = False
    return False

print(can_sum(4, [1, 3]))
print(can_sum(7, [5, 4, 3, 7]))
print(can_sum(7, [2, 4]))
print(can_sum(8, [2, 3, 5]))
print(can_sum(300, [7, 14]))