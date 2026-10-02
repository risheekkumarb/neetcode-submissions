class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1: return nums[0]
        seen = {}
        def dfs(i,n):
            if i >= n: return 0
            if i in seen:return seen[i]
            res = max(nums[i]+dfs(i+2,n), dfs(i+1,n))
            seen[i] = res
            return res
        
        first_house = dfs(0,n-1)
        seen.clear()
        second_house = dfs(1,n)
        return max(first_house, second_house)
