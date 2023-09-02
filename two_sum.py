# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to the target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.You can return the answer in any order.

class Solution(object):
    def twoSum(self, nums, target):    
        for i in range(len(nums) - 1):
            j = i+1
            for j in range(i+1, len(nums)):
                print(j)
                try:
                    if(nums[i]+nums[j]==target):
                        out = [i,j]
                        return out
                except IndexError:
                    pass  
              

nums = [2,5,5,15]
target = 10  
two_sum = Solution()
print(two_sum.twoSum(nums, target)) 
