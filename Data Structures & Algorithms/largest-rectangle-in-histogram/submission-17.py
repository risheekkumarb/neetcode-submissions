class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = [] # maintain it in such a way that it monotoniously increasing
        
        leftMost = [0] * n
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]: stack.pop()
            if stack: leftMost[i] = stack[-1]+1
            stack.append(i)
        
        stack = []
        rightMost = [n-1] * n
        for i in range(n-1,-1,-1):
            while stack and heights[stack[-1]] >= heights[i]: stack.pop()
            if stack: rightMost[i] = stack[-1]-1
            stack.append(i)
        
        maxArea = 0
        for i in range(n):
            width  = rightMost[i] - leftMost[i] +1
            height = heights[i]
            maxArea = max(maxArea, height*width)
        
        return maxArea