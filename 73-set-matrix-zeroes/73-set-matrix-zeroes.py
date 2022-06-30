class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        positions = []
        for i in range (len(matrix)):
            for j in range (len(matrix[i])):
                if matrix[i][j] == 0:
                    positions.append ([i, j])
        for i in range (len(matrix)):
            for j in range (len(matrix[i])):
                for pos in positions:
                    if (i == pos[0]) or (j == pos[1]):
                        matrix[i][j] = 0
                
                
               