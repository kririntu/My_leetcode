class Solution(object):
    def permute(self, nums):
        if len(nums) == 0:
            return [[]]
        
        result = []
        for i in range(len(nums)):
            present = [nums[i]]
            rest = nums[:i] + nums[i+1:]
            
            for p in self.permute(rest):   # FIX HERE
                result.append(present + p)
        
        return result