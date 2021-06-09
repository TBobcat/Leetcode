## default leetcode answer format

class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        lst = [char for char in command]
        res = []
        lst_length=len(lst)
        
        i = 0
        while i < len(lst):
            if lst[i] == 'G':
                res.append('G')
                i+=1
                #print(res)
            elif lst[i] == "(":
                # slicing end index can go out of range
                if lst[i:i+2] == ['(', ')']:
                    res.append('o')
                    i+=2
                elif lst[i:i+4] == ['(', 'a', 'l', ')']:
                    res+=['a', 'l']
                    i+=4
            
        return "".join(res)