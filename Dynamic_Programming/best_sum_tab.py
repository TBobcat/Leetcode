
def best_sum(num, lst):
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
                ## if none value(default value) at later position,
                ## fill it up with add item list
                if populate[a+item] == None:
                    populate[a+item] = thing + [item]

                ## if already lists at later position, only fill it up
                ## with add item list if its length is shorter
                elif len(populate[a+item]) > len(thing+[item]):
                    populate[a+item] = thing + [item]

                ## above can be combined to 
                ## if None || len(populate[a+item]) > len(thing+[item])
                ## then fill in the item list
            else:
                continue
    
    return populate[num]


print(best_sum(8, [1,4,5]))     # [4,4]
print(best_sum(8, [2,3,5]))
print(best_sum(7, [4, 5, 3, 7])) # [7]
print(best_sum(4, [1, 3])) 
print(best_sum(7, [5, 4, 3, 7]))
print(best_sum(7, [2, 4]))
print(best_sum(8, [3, 5, 2]))
print(best_sum(300, [7, 14]))
