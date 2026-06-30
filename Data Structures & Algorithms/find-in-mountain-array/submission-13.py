class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        l,r = 0, n-1

        while l<r:
            m = (l+r) // 2
            leftNum, rightNum = mountainArr.get(m), mountainArr.get(m+1)
            if rightNum > leftNum: l = m+1
            else: r = m
        
        peak = l
        l,r  = 0, peak

        while l<=r:
            m = (l+r)//2
            mid = mountainArr.get(m)
            if mid == target: return m
            elif target > mid: l = m+1
            else: r = m-1

        l,r  = peak, n-1 
        while l<=r:
            m = (l+r)//2
            mid = mountainArr.get(m)
            if mid == target: return m
            elif target < mid: l = m+1
            else: r = m-1
        
        return -1
        