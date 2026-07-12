class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
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

        res = ['']
        
        for d in digits: # '3'
            temp = []
            for o in res:
                for m in mapping[d]: temp.append(o+m)
            res = temp[:]

        return res