class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        # find zeroes
        # determine which rows and columns to be zero
        # then make it zero

        m,n = len(matrix),len(matrix[0])
        zeros = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0: zeros.append((i,j))

        rows,cols = set(),set()
        for i,j in zeros: rows.add(i),cols.add(j)

        for i in range(m):
            for j in range(n):
                if i in rows: matrix[i][j] = 0
                if j in cols: matrix[i][j] = 0
                