from collections import Counter
class Solution:
    def first(self,x): return x[0]
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return list(map(self.first, Counter(nums).most_common(k)))