class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        flags = [False] * n
        res = []
        path = []

        def dfs():
            if len(path) == n:
                res.append(path[:])
                return
            for i in range(len(nums)):
                if flags[i]: continue
                if i and nums[i] == nums[i-1] and not flags[i-1]: continue
                flags[i] = True
                path.append(nums[i])
                dfs()
                path.pop()
                flags[i] = False

        dfs()
        return res