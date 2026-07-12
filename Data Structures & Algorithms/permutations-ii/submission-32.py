class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res, path = [], []
        n = len(nums)
        flags = [False] * n

        def dfs():
            if len(path) == n:
                res.append(path[:]) 
                return

            for i in range(n):
                if flags[i]: continue
                if i and nums[i] == nums[i-1] and not flags[i-1]: continue
                flags[i] = True
                path.append(nums[i])
                dfs()
                path.pop()
                flags[i] = False

        dfs()
        return res