class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        inds = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                e = board[i][j]
                if e == '.': continue
                ind_i, ind_j = i//3, j//3
                print(rows,cols)
                if e in rows[i] or e in cols[j] or e in inds[ind_i][ind_j]:
                    return False
                rows[i].add(e)
                cols[j].add(e)
                inds[ind_i][ind_j].add(e)

        return True
