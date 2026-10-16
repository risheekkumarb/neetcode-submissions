from heapq import heapify, heappop, heappush
from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks = [-o for o in Counter(tasks).values()]
        waits = [] # start time, rem tasks
        heapify(tasks)

        time = 0
        while tasks or waits:
            time +=1 
            if not tasks: time = waits[0][0]
            while waits and waits[0][0] <= time:
                task = +1
                if task: heappush(tasks, heappop(waits)[1])
            if not tasks: continue
            task = heappop(tasks)+1
            if task: heappush(waits, (time+n+1,task))
        return time