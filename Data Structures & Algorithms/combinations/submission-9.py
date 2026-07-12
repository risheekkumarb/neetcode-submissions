class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = list(range(1,n+1))
        res, path = [], []
        
        def dfs(i):
            if i >= n:
                if len(path) == k: res.append(path[:])
                return
            path.append(nums[i])
            dfs(i+1)
            path.pop()
            dfs(i+1)
        dfs(0)
        return res