
# tabulation method
# start analyzing problem by looking at the iteration graph on 
# can_sum_tab, and utilize that 
def how_sum(num, lst):
        # """
        # :type num: int
        # :type lst：List[int]
        # :rtype: List[int], or None
        # """
    populate = [ None for i in range(num+1)]
  
    # base case as to add up to 0, just pick nothing from lst,
    # aka empty list, which is valid solution for 0
    populate[0] = []

    for a, thing in enumerate(populate):
        for i, item in enumerate(lst):
            if a +item <= len(populate)-1 and thing != None:
                populate[a+item] = thing+[item]
            else:
                continue
    
    return populate[num]


print(how_sum(4, [1, 3]))           
print(how_sum(7, [5, 4, 3, 7]))     
print(how_sum(7, [2, 4]))            
print(how_sum(7, [2, 5]))           
print(how_sum(8, [2, 3, 5]))        
print(how_sum(300, [7, 14]))         

print(how_sum(7, [2,3]))


# time complexity
# m = num, n = lst length
# 2 for loops, so m iteration in outter loop, n iteration in innter loop
# and for each of these 2 iterations, coping 'thing' which could be 
# a list of m elements(m 1s)
# so O(m * n * m) = O(nm^2)

# space complexity
# length of populate = m, with each index can have worst m items' list (m 1s)
# so O(m * m) = O(m^2)





