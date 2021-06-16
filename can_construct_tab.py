
def can_construct(str, str_lst):

    #[''] is base case here
    result = list(map(lambda x: (x, False), [''] + list(str)))
    print(result)
    result[0] = ('', True)

    for i, char in enumerate(result):
        if (i < len(result) -1  
            and result[i][0] == True 
            and result[i+1][0] in str_lst):
            
            result[i+1][1] = True


    return result[-1][1]


print(can_construct('', ['ab', 'abc', 'cd', 'def', 'abcd']))    # True
print(can_construct('ab', ['ab', 'abc', 'cd', 'def', 'abcd']))  # True
# print(can_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))  # True