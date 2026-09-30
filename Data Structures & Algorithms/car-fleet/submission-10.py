class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        for p,s in zip(position,speed): stack.append((p,s))
        stack = sorted(stack, key=lambda x: x[0])
        
        fleets = 0
        lowest_time = float('-inf')
        while stack:
            p,s = stack.pop()
            time = (target - p) / s
            if time > lowest_time:
                fleets += 1
                lowest_time = time

        return fleets