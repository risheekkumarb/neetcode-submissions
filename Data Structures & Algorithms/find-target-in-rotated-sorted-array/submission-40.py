class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1

        while l<r:
            m = (l+r) // 2
            if nums[m] > nums[r]: l = m+1
            else: r = m
        
        pivot = r
        l,r = 0,len(nums)-1
        if pivot >0 and nums[0] <= target <= nums[pivot-1]: r = pivot-1
        else: l = pivot

        while l<=r:
            m = (l+r) // 2
            if nums[m] == target: return m
            elif nums[m] > target: r = m-1
            else: l = m+1
        return -1