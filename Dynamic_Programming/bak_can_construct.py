def can_construct(target, word_bank):
    if target == "":
        return True
    for word in word_bank:
        if len(target) >= len(word) and target[: len(word)] == word:
            remainder = target[len(word) :]
            print(remainder)
            if can_construct(remainder, word_bank):
                return True
    return False




print(can_construct('ab', ['ab'])) #True
print(can_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(can_construct('abcdef', ['ab', 'abc', 'def', 'abcd']))   # True