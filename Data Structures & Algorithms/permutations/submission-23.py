class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        self.ans = []
        used = [False] * n

        def dfs(path):
            if len(path) == n:
                self.ans.append(path[:])
                return
            
            for i in range(n):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    dfs(path)
                    path.pop()
                    used[i] = False

        dfs([])
        return self.ans