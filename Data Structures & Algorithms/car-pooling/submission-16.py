from heapq import heappush, heapify, heappop
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # init with start, people, to - maintain a min_heap
        min_heap = [(f,p,t,i) for i, (p,f,t) in enumerate(trips)] # i - tie breaker
        heapify(min_heap)
        # keep track of capacity
        # increment distance
        cur = 0
        incar  = [] # to, p
        while min_heap:
            # drop when distance is reached - to. increase cap
            while incar and cur == incar[0][0]:
                t,p,i = heappop(incar)
                capacity += p
                # if cap less than 0 break and return False
            while min_heap and cur == min_heap[0][0]:
                # pick up when distance is equal - from. reduce cap
                f,p,t,i = heappop(min_heap)
                heappush(incar, (t,p,i))
                capacity -= p
                if capacity < 0: return False
            cur += 1
        
        return True