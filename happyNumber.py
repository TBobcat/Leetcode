def isHappy(n):
    """
    :type n: int
    :rtype: bool
    """
    #returns the list of digits that makes up the number
    s = set()
    summ=sum([int(dig)**2 for dig in str(n)])

    while summ != 1:
        print(summ)
        if summ in s:
            return False
        else:
            s.add(summ)
            summ=sum([int(dig)**2 for dig in str(summ)])
    return True



if __name__ == '__main__':
    num1=19
    num2=2

    print(isHappy(num1))
    print(isHappy(num2))

else:
    pass