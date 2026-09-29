class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []

        for i, num in enumerate(nums):
            if num > 0: break
            if i>0 and nums[i-1]==num: continue
            l,r = i+1,n-1
            while l < r:
                csum = num + nums[l] + nums[r]
                if csum == 0:
                    ans.append([num,nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l] == nums[l-1]: l += 1
                    while l<r and nums[r] == nums[r+1]: r -= 1
                elif csum > 0: r-=1
                else: l+=1
        return ans