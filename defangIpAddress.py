def defangIPaddr(address):
    """
    :type address: str
    :rtype: str
    """

    ## use list(str) and str.join(list_str)
    ## join can also be used like this
    ## 'abc'.join(address1.split('.')) -> '1abc1abc1abc1'
    ## str.replace() would also be useful
    res = ""
    list_address = list(address)
    for i,char in enumerate(list_address):
        if char == ".":
            list_address[i] = "[.]"

    res = res.join(list_address)
    return res


if __name__ == '__main__':
    address1 = "1.1.1.1"
    address2 = "255.100.50.0"

    print(defangIPaddr(address1))
    print(defangIPaddr(address2))

else:
    pass