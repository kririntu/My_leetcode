import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        nums = [-s for s in nums]
        heapq.heapify(nums)
        for i in range(k):
            y = -heapq.heappop(nums)
        return y
        