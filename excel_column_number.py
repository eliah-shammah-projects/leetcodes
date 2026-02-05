# Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

class Solution:
    def titleToNumber(self, columnTitle): 
        sum = 0
        for i in range (len(columnTitle)):
            sum = sum*26 + (ord(columnTitle[i]) - 64)
        return sum
    
    