class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0: return []
        mapping = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz',
        }
        self.ans = []

        def dfs(i,path):
            if i >= len(digits):
                self.ans.append(''.join(path))
                return

            for child in mapping[digits[i]]:
                path.append(child)
                dfs(i+1,path)
                path.pop()

        dfs(0,[])
        return self.ans