class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def chk(target):
            csum = 0
            g = 1
            for num in nums:
                csum += num
                if csum > target:
                    g += 1
                    if g > k: return False
                    csum = num
            return True
        
        l,r = max(nums), sum(nums)
        res = r
        while l <= r:
            m = (l+r) // 2
            if chk(m):
                res = m
                r = m-1
            else: l = m+1
        
        return res