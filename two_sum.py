# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

class Solution:
    def twoSum(self, nums, target: int):
        dict_help = {}
        for i, j in enumerate(nums):
            diff = target - j
            if diff in dict_help:
                return [i, dict_help[diff]]
            else:
                dict_help[j] = i

           






        