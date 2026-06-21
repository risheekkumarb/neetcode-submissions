from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        buckets = [[] for i in range(len(nums)+1)]

        for num, freq in counts.items():
            buckets[freq].append(num)
        
        res = []
        for bucket in buckets[::-1]:
            for item in bucket:
                res.append(item)
                if len(res) == k: return res
                