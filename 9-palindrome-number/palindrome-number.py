class Solution(object):
    def isPalindrome(self, x):
      
        # Negative numbers are not palindrome
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_num = 0
        # Reverse only half of the number
        while x > reversed_num:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10
        
        # Check for both even and odd length numbers
        return x == reversed_num or x == reversed_num // 10

        