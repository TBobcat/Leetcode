def uniqueOccurrences(arr):
    """
    :type arr: List[int]
    :rtype: bool
    """
    ## flip the count dict. with values and key list
    ## if original kays have duplicate values, make it a value:[key1, key2]
    ## if len key list > 1, return False
    d = {}
    
    for num in arr:
        if num in d:
            d[num] += 1
        else:
            d[num] = 1
    
    print(d)
    flipped_d = {}
    
    for k,v in d.items():
        if v not in flipped_d:
            flipped_d[v] = [k]
        else:
            flipped_d[v].append(k)
        
        if len(flipped_d[v]) > 1:
            return False
        else:
            continue
    
    return True

if __name__ == "__main__":
    print(uniqueOccurrences([1,2]))