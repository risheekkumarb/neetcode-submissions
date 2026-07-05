from collections import Counter
from heapq import heappop, heapify, heappush
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks = [-o for o in Counter(tasks).values()]
        waits = []
        heapify(tasks); heapify(waits)

        # looop
        ## check if any waits is over and add it to tasks
        ## take the highest freq task in the tasks
        ## decrement its count, if count > 0 add it to waits
        t = 0
        while tasks or waits:
            t += 1
            while waits and waits[0][0] <= t:
                time, cnt = heappop(waits)
                heappush(tasks, (cnt))
            if not tasks: continue
            cnt = 1 + heappop(tasks)
            if cnt: heappush(waits, (t+n+1,cnt))
        return t