def kidsWithCandies(candies, extraCandies):
    """
    :type candies: List[int]
    :type extraCandies: int
    :rtype: List[bool]
    """
    max_candy=sorted(candies, reverse=True)[0]
    result = map(lambda x: x+extraCandies >= max_candy, candies)

    return list(result)





if __name__ == '__main__':
    candies1 = [2,3,5,1,3]
    extraCandies1 = 3

    candies2 = [4,2,1,1,2]
    extraCandies2 = 1

    candies3 = [12,1,12]
    extraCandies3 = 10

    print(kidsWithCandies(candies1, extraCandies1))
    print(kidsWithCandies(candies2, extraCandies2))
    print(kidsWithCandies(candies3, extraCandies3))

else:
    pass