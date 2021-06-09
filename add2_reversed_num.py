
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def addTwoNumbers(l1,l2):
    # syntax need to return sth before the loop
    string_l1=[str(int) for int in l1]
    string_l2=[str(int) for int in l2]

    #print(string_l1)
    str_of_l1="".join(string_l1)
    str_of_l2="".join(string_l2)

    #print(str_of_l1)
    int1 = int(str_of_l1[::-1])
    int2 = int(str_of_l2[::-1])

    res = int1+int2
    print('sum is', res)
    return [char for char in str(res)]





if __name__ == '__main__':
    l1 = [2,4,3]
    l2 = [5,6,4]

    print(addTwoNumbers(l1,l2))

    l3=[0]
    l4=[0]

    print(addTwoNumbers(l3,l4))

    l5 = [9,9,9,9,9,9,9]
    l6 = [9,9,9,9]

    print(addTwoNumbers(l5,l6))

else:
    pass