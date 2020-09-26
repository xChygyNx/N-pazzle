from typing import List


class FormatState:
	@classmethod
	def matrix_to_list(cls, matrix: List[List[int]]) -> List[int]:
		result = []
		for i in range(len(matrix)):
			for j in range(len(matrix[i])):
				result.append(matrix[i][j])
		return result
