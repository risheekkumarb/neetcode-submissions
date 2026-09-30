class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1

        while l < r:
            m = (l+r)//2
            if nums[m] > nums[r]: l = m+1
            else: r =m
        
        pivot = l
        l,r = 0,len(nums)-1
        if nums[pivot] <= target <= nums[r]: l = pivot
        else: r = pivot-1 if pivot > 0 else r

        # print(l,r,pivot)
        res = 0
        while l <= r:
            m = (l+r) // 2
            if nums[m] <= target: l = m+1
            else: r = m-1

        return r if nums[r] == target else -1