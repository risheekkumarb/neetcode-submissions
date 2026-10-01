class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        used  = [False] * n
        ans = []

        def dfs(i, path):
            if len(path) == len(nums):
                ans.append(path[:])
                return
            for j in range(n):
                if not used[j]:
                    used[j] = True
                    path.append(nums[j])
                    dfs(j+1,path)
                    path.pop()
                    used[j] = False
        dfs(0,[])
        return ans