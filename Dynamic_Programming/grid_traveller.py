## tabulation grid traveller
## returns total number of ways travelling to (m,n)

def grid_traveller(m,n):
    ## create a 2d list m x n list
    d = [ [0]*(n+1) for item in range(m+1)]
    #print(d)

    d[1][1] = 1
    for i in range(m+1):
        for j in range(n+1):
            #print(i,j)
            if i+1 <= m: 
                d[i+1][j] += d[i][j]
            if j+1 <=n:
                d[i][j+1] += d[i][j]


    #print(d)
    return d[m][n]


print(grid_traveller(1,1))  # 1
print(grid_traveller(2,3))  # 3
print(grid_traveller(3,2))  # 3
print(grid_traveller(3,3))  # 6
print(grid_traveller(18,18))  # 2333606220