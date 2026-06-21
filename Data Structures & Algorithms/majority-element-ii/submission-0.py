from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        t = len(nums) // 3
        return [k for k,v in Counter(nums).items() if v > t]