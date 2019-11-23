class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        rows = len(matrix)
        cols = len(matrix[0])
        # 0,0 to row-1,col-1
        # diagonal elements (2,0); (1,0) (2,1); ()
        # 0,0; 0,1; 0,2; 0,3
        # 1,0; 2,0
        for i in range(cols):
            row, col = 0, i
            val = matrix[row][col]
            while row + 1 < rows and col + 1 < cols:
                if matrix[row + 1][col + 1] != val:
                    return False
                row, col = row + 1, col + 1
        for j in range(1, rows):
            row, col = j, 0
            val = matrix[row][col]
            while row + 1 < rows and col + 1 < cols:
                if matrix[row + 1][col + 1] != val:
                    return False
                row, col = row + 1, col + 1
        return True

s = Solution()
print(s.isToeplitzMatrix([[1,2],[2,2]]))