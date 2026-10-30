class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = []
        for i, num in enumerate(nums):
            A.append([num,i])
        A.sort()

        l,r = 0,len(nums)-1
        while l<r:
            csum = A[l][0] + A[r][0]
            if csum == target:
                return [min(A[l][1],A[r][1]), max(A[l][1],A[r][1])]
            elif csum < target:
                l += 1
            else:
                r -= 1
        return -1 