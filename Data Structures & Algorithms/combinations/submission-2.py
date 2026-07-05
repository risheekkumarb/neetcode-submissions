class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = list(range(1,n+1))
        res = []

        def dfs(i,path):
            if len(path) == k:
                res.append(path[:])
                return
            if i >= n:
                return
            path.append(nums[i])
            dfs(i+1,path)
            path.pop()
            dfs(i+1,path)

        dfs(0,[])
        return res