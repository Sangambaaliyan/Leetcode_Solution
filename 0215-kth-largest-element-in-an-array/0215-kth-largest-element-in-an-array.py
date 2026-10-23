import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        m=[]
        for i in nums:
            heapq.heappush(m,i)
            if len(m)>k:
                heapq.heappop(m)
        return m[0]
        
        