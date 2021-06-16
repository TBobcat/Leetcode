class Solution(object):
    def replaceDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        # confirm input is filling the requirement of question
        # otherwise need error handling

        s_list=[char for char in s]
    
        for i,num in enumerate(s_list):
            if i % 2 !=0:
                s_list[i] = chr(ord(s_list[i-1])+int(num))
        
        print(s_list)
        return ''.join(s_list)

        # also python can't do string mutation through indexing, need a list
        # step i every 2 in loop to make it faster    
        # for i in range(1, len(s), 2):
        #       num = s_list[i]
        #       s_list[i] = chr(ord(s_list[i-1])+int(num))
                
        # return ''.join(s_list)