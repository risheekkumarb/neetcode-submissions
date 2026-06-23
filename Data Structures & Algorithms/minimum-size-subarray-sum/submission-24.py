class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        csum, l = 0, 0
        res = float('inf')

        for r, num in enumerate(nums):
            csum += num
            while csum >= target:
                if csum >= target: res = min(res, r-l+1)
                csum -= nums[l]
                l += 1
        return 0 if res == float('inf') else res
