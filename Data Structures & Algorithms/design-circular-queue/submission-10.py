class ListNode:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self): return f'(val={self.val}, left={self.left}, right={self.right})'

class MyCircularQueue:
    def __init__(self, k: int):
        self.cap = k
        self.cur = 0
        self.left, self.right = ListNode(0), ListNode(0)
        self.left.right, self.right.left = self.right, self.left

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        new_node = ListNode(value)
        new_node.left, new_node.right = self.right.left, self.right
        self.right.left.right, self.right.left = new_node, new_node
        self.cur += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        node = self.left.right
        node.right.left, node.left.right = node.left, node.right
        self.cur -= 1
        return True

    def Front(self) -> int:
        return self.left.right.val if not self.isEmpty() else -1

    def Rear(self) -> int:
        return self.right.left.val if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        return self.cur == 0

    def isFull(self) -> bool:
        return self.cur == self.cap


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()