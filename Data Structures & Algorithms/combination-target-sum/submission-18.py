class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []

        def dfs(i,path,csum):
            if csum == target:
                ans.append(path[:])
                return
            if i == len(nums): return

            for j in range(i,len(nums)):
                if csum + nums[j] > target: continue
                path.append(nums[j])
                dfs(j,path,csum+nums[j])
                path.pop()

        dfs(0,[],0)
        return ans