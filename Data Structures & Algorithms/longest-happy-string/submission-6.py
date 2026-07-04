from heapq import heappush, heapify, heappop
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ''
        min_heap = []
        for cnt, char in [(-a,'a'),(-b,'b'),(-c,'c')]:
            if cnt != 0: heappush(min_heap, (cnt,char))

        while min_heap:
            cnt,let = heappop(min_heap) # r neg
            if len(res) > 1 and res[-1] == res[-2] == let:
                if not min_heap: break
                scnt,slet = heappop(min_heap)
                res += slet
                scnt+=1
                if scnt: heappush(min_heap, (scnt,slet))
                heappush(min_heap, (cnt,let))
            else:
                res += let
                cnt += 1
                if cnt: heappush(min_heap, (cnt, let))
        return res

