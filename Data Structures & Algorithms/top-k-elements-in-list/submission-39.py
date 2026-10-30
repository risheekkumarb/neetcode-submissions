from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        counts = Counter(nums)
        buckets = [[] for _ in range(n+1)]

        for val,cnt in counts.items():
            buckets[cnt].append(val)

        res = []
        for bucket in buckets[::-1]:
            for val in bucket:
                res.append(val)
                if len(res) == k: return res