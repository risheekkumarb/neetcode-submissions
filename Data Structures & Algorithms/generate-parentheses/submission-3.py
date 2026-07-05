class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # path, open, closes
        # return if closes > opens or opens > n
        # make sure opens >= closes before adding another layer

        res = []

        def dfs(path,opens,closes):
            if opens == n and closes == n:
                res.append(''.join(path))
                return
            
            if opens < n:
                path.append('(')
                dfs(path,opens+1,closes)
                path.pop()
            if opens > closes:
                path.append(')')
                dfs(path,opens,closes+1)
                path.pop()

        dfs([],0,0)
        return res