from heapq import heapify, heappush, heappop
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # build minHeap
        minHeap = [(e,p,i) for i,(e,p) in enumerate(tasks)] # [(1,4,1),(3,3,2),(2,1,3)]
        heapify(minHeap)
        time = 0
        res = []

        ready = [] # (p,i)
        while minHeap or ready:
            while minHeap and minHeap[0][0] <= time:
                e,p,i = heappop(minHeap)
                heappush(ready, (p,i))
            if not ready:
                time = minHeap[0][0]
                continue
            p,i = heappop(ready)
            time += p
            res.append(i)

        return res