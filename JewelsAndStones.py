def numJewelsInStones(jewels, stones):
    """
    :type jewels: str
    :type stones: str
    :rtype: int
    """
    return sum(s in jewels for s in stones )













if __name__ == "__main__":
    jewels1 = "aA"
    stones1 = "aAAbbbb"
    jewels2 = "z"
    stones2 = "ZZ"

    print(numJewelsInStones(jewels1, stones1))
    print(numJewelsInStones(jewels2, stones2))

else:
    pass