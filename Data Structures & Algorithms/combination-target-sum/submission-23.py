class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []

        def dfs(i,path,csum):
            if csum == target:
                ans.append(path[:])
                return
            if i >= len(nums) or csum > target: return
            path.append(nums[i])
            dfs(i,path,csum+nums[i])
            path.pop()
            dfs(i+1,path,csum)

        dfs(0,[],0)
        return ans