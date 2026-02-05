# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        flag = False
        s2 = ""
        for i in range (len(s) - 1, -1, -1):
            if s[i] != " ":
                flag = True
                count += 1
            elif s[i] == " " and flag: 
                return count 
        return count





               
