class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        def dfs(i,csum,path):
            if i >= n or csum > target: return
            if csum == target:
                res.append(path[:])
                return
            for i in range(i,n):
                if csum + nums[i] > target: continue
                path.append(nums[i])
                dfs(i,csum+nums[i],path)
                path.pop()

        dfs(0,0,[])
        return res