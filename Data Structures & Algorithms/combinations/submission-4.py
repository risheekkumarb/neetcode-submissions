class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = list(range(1,n+1))
        res = []

        def dfs(i,path):
            if len(path) == k:
                res.append(path[:])
                return
            for j in range(i,n):
                path.append(nums[j])
                dfs(j+1,path)
                path.pop()

        dfs(0,[])
        return res