class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        flags = [False] * n
        res, path = [], []

        def dfs():
            if len(path) == n:
                res.append(path[:])
                return
            for i in range(n):
                if flags[i]: continue
                flags[i] = True
                path.append(nums[i])
                dfs()
                flags[i] = False
                path.pop()

        dfs()
        return res