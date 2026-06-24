class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        self.stack.append(price)
        i = len(self.stack)-1
        print(i)
        count = 0
        while i >= 0:
            if self.stack[i] <= price: count +=1
            else: break
            i -= 1

        return count

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)