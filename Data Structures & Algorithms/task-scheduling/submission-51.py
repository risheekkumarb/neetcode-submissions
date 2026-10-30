from heapq import heapify, heappop, heappush
from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks = [-o for o in Counter(tasks).values()]
        heapify(tasks)
        min_heap = [] # (time, tasks rem)
        time = 0
        while min_heap or tasks:
            time += 1
            if not tasks and min_heap[0][0] > time:
                time = min_heap[0][0]
            while min_heap and min_heap[0][0] <= time:
                heappush(tasks, heappop(min_heap)[1])
            rem = heappop(tasks)+1
            if rem: heappush(min_heap, (time+n+1,rem))

        return time