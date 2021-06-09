def maximumWealth(accounts):
    """
    :type accounts: List[List[int]]
    :rtype: int
    """
    wealth=0

    for i,lst in enumerate(accounts):
        sum = 0
        ## this can be done with the sum() function
        for num in lst:
            sum += num
        ## this can be done with the max() function
        ## using built in functions are generally 
        ## more run time efficient
        if sum > wealth:
            wealth = sum

    return wealth

# def maximumWealth(accounts):
# 	maxWealth = 0
# 	for i,lst in enumerate(accounts):
# 		totalWealth = sum(accounts[i])
# 		maxWealth = max(maxWealth, totalWealth)
# 	return maxWealth

if __name__ == '__main__':
    accounts1 = [[1,2,3],[3,2,1]]
    accounts2 = [[1,5],[7,3],[3,5]]
    accounts3 = [[2,8,7],[7,1,3],[1,9,5]]

    print(maximumWealth(accounts1))
    print(maximumWealth(accounts2))
    print(maximumWealth(accounts3))

else:
    pass