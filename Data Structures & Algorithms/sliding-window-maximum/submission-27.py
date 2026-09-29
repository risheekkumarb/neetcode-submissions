from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        wind = deque()
        res = []

        for r, n in enumerate(nums):
            # Remove the outgoing value if it is still in the deque.
            if r >= k and wind[0] == nums[r - k]:
                wind.popleft()

            # Keep values in decreasing order.
            while wind and wind[-1] < n:
                wind.pop()

            wind.append(n)

            if r >= k - 1:
                res.append(wind[0])

        return res