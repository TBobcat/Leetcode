

## using memoization
def can_construct(target, word_bank):
    memo = {}

    def helper(target, word_bank):
        if target == "":
            return True
        if target in memo:
            return memo[target]
        for word in word_bank:
            if len(target) >= len(word) and target[: len(word)] == word:
                remainder = target[len(word) :]
                if helper(remainder, word_bank):
                    memo[target] = True
                    return memo[target]
        memo[target] = False
        return False

    return helper(target, word_bank)




print(can_construct('ab', ['ab'])) #True
print(can_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'])) # True
print(can_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'])) # False
print(can_construct('abcdef', ['ab', 'abc', 'def', 'abcd']))   # True
print(can_construct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'])) # True
print(can_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'eee', 'eeee', 'eeeee']))
