# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        for i in s:
            if i.isalnum():
                new_s += i.lower()

        if new_s == new_s[::-1]:
            return True
        
        return False
    


        