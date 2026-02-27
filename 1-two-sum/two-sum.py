class Solution(object):
    def twoSum(self, nums, target):
        mem = {}
        for i,n in enumerate(nums):
            rest = target-n
            if rest in  mem:
                return [mem[rest],i]
            mem[n] = i              
            
            

            