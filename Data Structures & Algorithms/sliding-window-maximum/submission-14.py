from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # add elements to maintain a monotonic decreasing stack
        stack, res = deque([]), []
        l = 0

        for r, num in enumerate(nums):
            while stack and num > nums[stack[-1]]: stack.pop()
            stack.append(r)
            if l > stack[0]: stack.popleft()
            if r+1 >= k:
                res.append(nums[stack[0]])
                l += 1

        return res