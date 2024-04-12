class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transposed_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
        return transposed_matrix
