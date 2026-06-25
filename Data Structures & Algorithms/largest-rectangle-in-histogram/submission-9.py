class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = [] # maintain it in such a way that it monotoniously increasing
        res = 0

        for i in range(n+1):
            while stack and (i==n or heights[stack[-1]] >= heights[i]):
                height = heights[stack.pop()]
                width  = i if not stack else i-stack[-1]-1
                res = max(res, height * width)
            stack.append(i)

        return res