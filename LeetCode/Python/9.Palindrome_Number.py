#lc_9:02_02_2025
#https://leetcode.com/problems/palindrome-number/description/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x > 0 and x%10 == 0):
            return False
        rev = 0
        tmp = x
        if x < 0:
            return False
        while x > rev:
            mod = x % 10
            rev = rev * 10 + mod
            x = x // 10
        
        return x == rev or x == rev // 10       
