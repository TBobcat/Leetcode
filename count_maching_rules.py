## how to put helper function in python for leetcode questions

def check_list(lst, key, val):
    if (
            (key == 'type' and val == lst[0])
            or (key == 'color' and val == lst[1])
            or (key =='name' and val == lst[2])
        ):
        return True

class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        
        counter = 0
        for item in items:
            if check_list(item, ruleKey, ruleValue) == True:
                counter+=1
            else:
                continue
        
        return counter