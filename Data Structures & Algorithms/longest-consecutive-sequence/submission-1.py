class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 0
        seen  = set(nums)

        for num in nums:
            curr_count = 1
            if num+1 not in seen:
                while num-1 in seen:
                    curr_count += 1
                    num -= 1
                count = max(curr_count, count)

        return count