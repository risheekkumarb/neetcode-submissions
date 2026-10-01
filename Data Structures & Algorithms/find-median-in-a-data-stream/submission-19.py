from heapq import heappop,heappush,heapify
class MedianFinder:

    def __init__(self):
        self.small = [] # smaller numbers in -ve
        self.large = [] # larger  numbers in +ve

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heappush(self.large, num)
        else:
            heappush(self.small, -num)
        if len(self.small) > len(self.large)+1:
            val = -heappop(self.small)
            heappush(self.large, val)
        elif len(self.large) > len(self.small)+1:
            val = heappop(self.large)
            heappush(self.small, -val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large): return -self.small[0]
        elif len(self.large) > len(self.small): return self.large[0]
        else: return (-self.small[0] + self.large[0]) / 2.0
        