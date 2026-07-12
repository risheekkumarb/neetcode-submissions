class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res, n = [], len(nums)
        path = []

        def dfs(i, csum):
            if target == csum:
                res.append(path[:])
                return
            for j in range(i,n):
                if csum + nums[j] > target: continue
                path.append(nums[j])
                dfs(j, csum+nums[j])
                path.pop()

        dfs(0,0)
        return res