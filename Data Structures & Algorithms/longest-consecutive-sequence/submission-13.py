class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        ans = 0

        for num in nums:
            count = 1
            if num-1 not in num_set:
                while num+1 in num_set:
                    count += 1
                    num += 1
                ans = max(count,ans)

        return ans