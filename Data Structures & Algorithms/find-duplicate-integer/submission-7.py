class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        arr = set()
        for n in nums:
            if n in arr: return n
            arr.add(n)