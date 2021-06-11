#!/usr/bin/env python3

## return null if doesn't addup
## or list numbers of any choice that does add up
def how_sum(n, lst):
    memo={}
    return helper(n, lst, memo)

def helper(n, lst, m):
    if n in m:
        return m[n]
    if n == 0:
        return []
    if n < 0:
        return None

    for num in lst:
        remain = n - num
        result = helper(remain, lst, m) 
        if result != None:
            result.append(num)
            m[n] = result
            return result
    m[n] = None
    return None

# Brute Force
# time: O(n^m*m) for result.append(num)
# space: O(m)
#
# Memoization:
# time: O(n*m*m), o*m because no duplication
# space: O(m*m) m keys, whose value is a list that has most m length numbers

print(how_sum(4, [4]))
print(how_sum(4, [1, 3])) 
print(how_sum(7, [5, 4, 3, 7]))
print(how_sum(7, [2, 4]))
print(how_sum(8, [3, 5, 2]))
print(how_sum(300, [7, 14]))