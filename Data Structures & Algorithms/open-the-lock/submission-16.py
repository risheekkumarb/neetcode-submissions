from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visit = set(deadends)
        if "0000" in visit: return -1
        queue = deque([("0000", 0)])
        visit.add("0000")

        while queue:
            curr, turns = queue.popleft()
            if curr == target: return turns
            for i in range(4):
                for direction in (-1, 1):
                    digit = (int(curr[i]) + direction) % 10
                    nxt = curr[:i] + str(digit) + curr[i + 1:]

                    if nxt not in visit:
                        visit.add(nxt)
                        queue.append((nxt, turns + 1))

        return -1