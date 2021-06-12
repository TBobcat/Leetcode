
# can sum tabulation
def can_sum(num, lst):

## can't use dictionary as each key has no numeric relationship
## to be incremented 

    # this should be list of True AANNDD False
    # indexed 0 ~ num, meaning at index i of populate,
    # number i can be sumed by nums in list or not
    populate = [False for i in range(num+1)]
  
    # base case as to add up to 0, just pick nothing from lst,
    # which is valid
    populate[0] = True

    for a, thing in enumerate(populate):
        for i, item in enumerate(lst):
            if a +item <= len(populate)-1 and thing == True:
                populate[a+item] = True
    
    return populate[num]

print(can_sum(4, [1, 3]))            #True
print(can_sum(7, [5, 4, 3, 7]))      #True
print(can_sum(7, [2, 4]))            #False
print(can_sum(7, [2, 5]))            #True
print(can_sum(8, [2, 3, 5]))         #True
print(can_sum(300, [7, 14]))         #False