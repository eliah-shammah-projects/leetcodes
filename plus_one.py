# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
# Increment the large integer by one and return the resulting array of digits.


class Solution:
    def plusOne(self, digits):

        carry = 1
        for i in range (len(digits) -1, 0 , -1):
            
            result = digits[i] + carry
            if result < 10:
                digits[i] = result
                carry = 0
            else:
                digits[i] = 0
                carry = 1
            
        result = digits[0] + carry 
        if result < 10:
            digits[0] = result 
        else:
            digits[0] = 0
            digits.insert(0,1)
        return digits
            
            

        