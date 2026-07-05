from collections import Counter
from heapq import heapify, heappop, heappush
class Solution:
    def reorganizeString(self, s: str) -> str:
        # dictionary of counter
        # maintain a maxHeap of (cnt, letter)
        maxHeap = [(-v,k) for k,v in Counter(s).items()] # [(-3,a),(-2,b)]
        heapify(maxHeap)
        res = ''
        # while loop till maxHeap is over
        while maxHeap:
            cnt, letter = heappop(maxHeap) # (-3,a)
            if cnt == 0: break
            elif len(res) > 0 and res[-1] == letter:
                if not maxHeap: return ''
                scnt, slet = heappop(maxHeap)
                scnt += 1
                res += slet
                if scnt: heappush(maxHeap, (scnt,slet))
            else:
                res += letter
                cnt += 1
            if cnt: heappush(maxHeap, (cnt,letter))
            # keep track of last letter using res 
            ### --> if last char is the most frequent use the second most freq
        return res if len(res) == len(s) else ''
