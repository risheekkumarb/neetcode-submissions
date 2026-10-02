class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        seen = {}
        def dfs(i):
            if i >= n: return 0
            if i in seen: return seen[i]
            res = nums[i] + max(dfs(i+2),dfs(i+3))
            seen[i] = res
            return res
        return max(dfs(0),dfs(1))