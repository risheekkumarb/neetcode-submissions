from heapq import heappop, heapify
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = [o*-1 for o in nums]
        heapify(max_heap)
        res = None
        for _ in range(k):
            res = heappop(max_heap)
        return -res