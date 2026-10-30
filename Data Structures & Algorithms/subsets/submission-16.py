class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []

        def dfs(i, path):
            if i >= len(nums):
                self.res.append(path[:])
                return
            path.append(nums[i])
            dfs(i+1,path)
            path.pop()
            dfs(i+1,path)

        dfs(0,[])
        return self.res