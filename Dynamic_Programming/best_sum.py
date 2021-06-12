#!/usr/bin/env python3

def best_sum(n, lst):
    memo={}
    return helper(n, lst, memo)

def helper(n, lst, m):
    if n in m:
        return m[n]
    if n == 0:
        return []
    # if n < 0:
    #     return None

    short = []
    for num in lst:
        remain = n - num

        if remain >= 0:
            result = helper(remain, lst, m) 
            if result != None:
                result.append(num)
                if len(short) == 0:
                    short = result
                elif len(result) < len(short):
                    short = result

                print(short)
        
    m[n] = short
    return m[n]
    

#print(best_sum(7, [7]))
print(best_sum(7, [4, 5, 3, 7]))
# print(best_sum(4, [1, 3])) 
# print(best_sum(7, [5, 4, 3, 7]))
# print(best_sum(7, [2, 4]))
# print(best_sum(8, [3, 5, 2]))
# print(best_sum(300, [7, 14]))