# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

 


class Solution:
    def singleNumber(self, nums) -> int:

        di ={}
        for i in nums:
            if i in di:
                di[i] += 1
            else:
                di[i] = 1
        for j,k in di.items():
            if k == 1:
                return j
            
        
        