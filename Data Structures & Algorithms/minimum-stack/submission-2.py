class MinStack:

    def __init__(self):
        self.stack     = [] # 1,2
        self.inc_stack = [] # 1,1

    def push(self, val: int) -> None:
        self.stack.append(val)
        inc_stack = self.inc_stack
        if inc_stack and val > inc_stack[-1]: inc_stack.append(inc_stack[-1])
        else: inc_stack.append(val)

    def pop(self) -> None:
        self.inc_stack.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.inc_stack[-1]
