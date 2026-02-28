class Solution(object):
    def threeSum(self, nums):
        res = set()
        n = len(nums)

        for i in range(n):
            seen = set()
            for j in range(i+1, n):
                rest = -nums[i] - nums[j]
                if rest in seen:
                    res.add(tuple(sorted([nums[i], nums[j], rest])))
                seen.add(nums[j])

        return [list(x) for x in res]

        