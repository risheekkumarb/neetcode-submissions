class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        flags = [False] * n

        res = []

        def dfs(i,path):
            if len(path) == n:
                res.append(path[:])
                return
            for j in range(0,n):
                if flags[j]: continue
                flags[j] = True
                path.append(nums[j])
                dfs(j,path)
                path.pop()
                flags[j] = False

        
        dfs(0,[]) # [1,2,3]
        return res