class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        real_num = abs(x)
        reverse = 0
        while(real_num != 0):
            remainder = real_num % 10
            reverse = reverse * 10 + remainder
            real_num = real_num // 10
            
        if abs(reverse) > 2**31 -1:
            return 0
        else:
            if x > 0:
                return reverse
            if x < 0:
                return -reverse
            else:
                return 0