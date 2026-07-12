class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nums.sort()
        tl = sum(nums)
        if tl % k != 0: return False

        l = tl / k
        sides = [0] * k

        def dfs(i):
            if i == len(nums):
                return all(o==p for o,p in zip(sides[:k-1],sides[1:]))
            
            for j in range(k):
                if sides[j] + nums[i] <= l:
                    sides[j] += nums[i]
                    if dfs(i+1): return True
                    sides[j] -= nums[i]
                if sides[j] == 0: break
            
            return False

        return dfs(0)