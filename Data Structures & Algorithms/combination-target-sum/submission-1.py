class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i,csum,path):
            if i >= len(nums) or csum > target: return
            if csum == target:
                res.append(path[:])
                return
            path.append(nums[i])
            dfs(i,csum+nums[i],path)
            path.pop()
            dfs(i+1,csum,path)

        dfs(0,0,[])
        return res