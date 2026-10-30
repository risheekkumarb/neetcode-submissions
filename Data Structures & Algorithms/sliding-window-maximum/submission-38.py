from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        stack = deque([])

        for i,num in enumerate(nums):
            while stack and nums[stack[-1]] <= num: stack.pop()
            stack.append(i)
            if stack[0] < i-k+1: stack.popleft()
            if i>=k-1: res.append(nums[stack[0]])
        
        return res