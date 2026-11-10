class Solution(object):
    def twoSum(self, nums, target):
        pairs = {}
        for i, number in enumerate(nums):
            comp = target - number
            
            if comp not in pairs:
                pairs[number] = i
            else:
                return [pairs[comp], i]
        return []