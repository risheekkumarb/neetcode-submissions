class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        n = len(nums)
        flags = [False] * n

        res = []

        def dfs(path):
            if len(path) == n:
                res.append(path[:])
                return
            
            for j in range(n):
                if not flags[j]:
                    if j and nums[j] == nums[j-1] and not flags[j-1]: continue
                    flags[j] = True
                    path.append(nums[j])
                    dfs(path)
                    flags[j] = False
                    path.pop()

        dfs([])
        return res