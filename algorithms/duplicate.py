##Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct.

class Solution(object): ## Solution O(n)
    def containsDuplicate(self, nums):
       hs = set(nums)
       if len(hs) != len(nums):
           return True
       return False

teste = Solution()

print(teste.containsDuplicate([1,2,3,4])) ##false
print(teste.containsDuplicate([1,2,3,4,4])) ##true


class Solution(object): ## Solution O(n^2) 
    def containsDuplicate(self, nums):
       for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                if nums[i] == nums[j]:
                    return True
            return False
