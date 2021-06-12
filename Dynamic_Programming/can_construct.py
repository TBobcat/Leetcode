

## brute force recursion
def can_construct(target, word_bank):
    if target == "":
        return True

    for word in word_bank:
        if target.startswith(word):
            remainder = target[len(word):]
        
            if can_construct(remainder, word_bank):
                return True
    return False




print(can_construct('ab', ['ab'])) #True
print(can_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'])) # True
print(can_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'])) # False
print(can_construct('abcdef', ['ab', 'abc', 'def', 'abcd']))   # True
print(can_construct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'])) # True
print(can_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'eee', 'eeee', 'eeeee']))
