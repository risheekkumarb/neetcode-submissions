class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nums.sort(reverse=True)
        tl = sum(nums)
        if tl % k != 0: return False

        l = tl // k
        used = [False] * len(nums)

        def dfs(i,k,subsetSum):
            if k == 0: return True
            if subsetSum == l: return dfs(0,k-1,0)        
            for j in range(i,len(nums)):
                if used[j] or subsetSum + nums[j] > l: continue
                used[j] = True
                if dfs(j+1,k,subsetSum+nums[j]): return True
                used[j] = False

                if subsetSum == 0: return False
            
            return False

        return dfs(0,k,0)