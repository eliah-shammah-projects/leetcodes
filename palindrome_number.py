# Given an integer x, return true if x is a palindrome, and false otherwise.

class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x >= 0: 
           return int("".join(reversed(str(x)))) == x
        else:
            return False
        