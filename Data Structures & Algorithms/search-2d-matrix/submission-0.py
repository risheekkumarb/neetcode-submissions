class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix), len(matrix[0])
        l,r = 0, m*n-1
        
        while l <= r:
            mid = (l+r) // 2
            row, col = mid//n, mid%n
            mid_elem = matrix[row][col]
            if mid_elem == target: return True
            elif target > mid_elem:
                l = mid+1
            else:
                r = mid-1
        
        return False