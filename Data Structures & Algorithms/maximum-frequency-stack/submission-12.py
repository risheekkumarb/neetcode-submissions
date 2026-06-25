from heapq import heappop, heappush
class FreqStack:

    def __init__(self):
        self.time = 0
        self.freq = {}
        self.max_heap = [] # (-freq, -time, elem)
        
    def push(self, val: int) -> None:
        self.time += 1
        self.freq[val] = self.freq.get(val, 0) + 1
        heappush(self.max_heap, (-self.freq[val], -self.time, val))

    def pop(self) -> int:
        _, _, val = heappop(self.max_heap)
        self.freq[val] -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()