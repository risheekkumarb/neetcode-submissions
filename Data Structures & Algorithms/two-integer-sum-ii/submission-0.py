class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0, len(numbers)-1

        while l < r:
            csum = numbers[l] + numbers[r]
            if csum == target: return [l+1,r+1]
            elif csum > target: r -= 1
            else: l += 1
        