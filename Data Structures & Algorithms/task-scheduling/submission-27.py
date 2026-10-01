from heapq import heapify, heappop, heappush
from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ts = [-o for o in Counter(tasks).values()] ## tasks left
        q = [] ## earliest time, tasks left
        heapify(ts)

        time = 0
        while ts or q:
            time +=1
            if not ts: time = max(time, q[0][0])
            while q and q[0][0] <= time: heappush(ts, heappop(q)[1])
            task = heappop(ts) + 1
            if task < 0: heappush(q, (time+n+1,task))            
        return time