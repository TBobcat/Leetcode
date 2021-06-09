# def compare_lists(l1, l2):
#     for a in l1:
#         if a not in l2:
#             return 


def longestWord(words):
    """
    :type words: List[str]
    :rtype: str
    """
    
    sorted_words=sorted(words)
    print(sorted_words)

    ## so the problem need to 2 variables to consider, length of word
    ## and whether word substring exists in the list
    string = sorted_words[0]
    word_set=set()

    # add "" to make sure char like 'd' is covered in below condition
    # cause 'd'[:-1] is ''
    # constructing from empty set here let's comparison make sure
    # only return string that has every 1 of its char in the set

    word_set.add("")

    for x in sorted_words:         
        if x[:-1] in word_set:
            if len(x) > len(string):
                string = x
            word_set.add(x)
    return string



if __name__ == "__main__":
    a = ["w","wo","wor","worl","world"]
    b = ["a","banana","app","appl","ap","apply","apple"]
    c = ["yo","ew","fc","zrc","yodn","fcm","qm","qmo","fcmz","z","ewq","yod","ewqz","y"]

    d = ["ogz","eyj","e","ey","hmn","v","hm","ogznkb","ogzn","hmnm","eyjuo","vuq","ogznk","og","eyjuoi","d"]
    print(longestWord(a))
    print(longestWord(b))
    print(longestWord(c))
    print(longestWord(d))

else:
    pass