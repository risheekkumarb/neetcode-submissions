class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        ans, n = 0, len(nums)
        seen = set()

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
