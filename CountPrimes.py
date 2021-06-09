def countPrimes( n):
    """
    :type n: int
    :rtype: int
    """
    prime_list=is_prime(n)

    # print(prime_list)

    return len(prime_list)


def is_prime(n):
    # based on Sieve of Eratosthenes

    result = []
    if n <=1 :
        return []  
    # Create a boolean array "prime[0..n]" and initialize
    # all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    prime = [True for i in range(n)]
    p = 2
    while (p * p <= n):
          
        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):
              
            # Update all multiples of p
            for i in range(p * 2, n , p):
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    # Print all prime numbers
    for p in range(n):
        if prime[p]:
            result.append(p) #Use print(p) for python 3
    
    return result


if __name__ == '__main__':
    num1=10
    num2=0
    num3=1

    # print(is_prime(0))
    # print(is_prime(1))
    # print(is_prime(2))

    print(countPrimes(num1))
    print(countPrimes(num2))
    print(countPrimes(num3))


else:
    pass