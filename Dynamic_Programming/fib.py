
# nth fib using memoization
def fib_1(n):
    memo = {0: 0, 1: 1}

    def helper(n):
        if n not in memo:
            memo[n] = helper(n - 1) + helper(n - 2)
        return memo[n]

    return helper(n)


# nth fib using tabulation
def fib_2(n):
    table = [0] * (n + 1)
    table[1] = 1

    for i in range(n - 1):
        table[i + 1] += table[i]
        table[i + 2] += table[i]

    # fill in last item in the list    
    table[-1] += table[-2]
    return table[-1]