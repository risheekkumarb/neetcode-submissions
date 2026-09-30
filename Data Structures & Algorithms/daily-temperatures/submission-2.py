class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # (i,temp)

        for i,t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                j,temp = stack.pop()
                res[j] = i-j
            stack.append((i,t))

        return res