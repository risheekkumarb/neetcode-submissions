class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        ans, n = 1, len(nums)
        seen = set()

        if n == 0: return 0

        for num in nums:
            if num-1 not in num_set:
                count = 1
                while num+1 in num_set:
                    count += 1
                    seen.add(num+1)
                    num += 1
                ans = max(ans, count)
            seen.add(num)

        return ans
