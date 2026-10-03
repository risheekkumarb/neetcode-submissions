class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1: return nums[0]
        seen = {}
        def dfs(i,n):
            if i >= n: return 0
            if i in seen: return seen[i]
            val = max(dfs(i+1,n), nums[i]+dfs(i+2,n))
            seen[i] = val
            return val

        start0 = dfs(0,n-1)
        seen.clear()
        start1 = dfs(1,n)

        return max(start0, start1)