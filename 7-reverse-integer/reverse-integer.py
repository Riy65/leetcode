class Solution(object):
    def reverse(self, x):
        sign = 1
        if x<0:
            sign = -1
        y= abs(x)
        result=0
        while y!=0:
            last_digit= y%10
            result = result*10 + last_digit
            y=y//10
        if  -2**31 <= result <= 2**31 - 1:
            return sign*result
        else:
            return 0
            