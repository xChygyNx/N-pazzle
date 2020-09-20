import os
from random import choice
from typing import List
from exceptions.exceptions import *
import config



class StateGenerator:
	def __init__(self, *, side: int = 0, file: str = None):
		self.side = side
		self.file = file
		self.source_state = self.set_source_state()
		self.target_state = self.set_target_state()

	def set_source_state(self) -> List[List[int]]:
		if self.file:
			matrix = self.get_state_from_file()
		else:
			matrix = [[0] * self.side for _ in range(self.side)]
			while True:
				plates = [x for x in range(self.side ** 2)]
				for i in range(self.side):
					for j in range(self.side):
						num = choice(plates)
						matrix[i][j] = num
						plates.remove(num)
				if self.exist_solution(matrix):
					break
		return matrix

	def set_target_state(self) -> List[List[int]]:
		matrix = self.snail_state()
		return matrix

	def exist_solution(self, state: List[List[int]]) -> bool:
		for i in range(len(state)):
			for j in range(len(state[i])):
				if state[i][j] == 0:
					line_with_void = 1 + i
		print(f'void in {line_with_void} lines')
		inversion = 0
		_list = self.matrix_to_list(state)
		for i in range(self.side ** 2):
			if not _list[i] == 0:
				for j in range(i + 1, self.side ** 2):
					if _list[i] > _list[j]:
						inversion += 1
		print(f"inversion = {inversion}")
		return (inversion + line_with_void) % 2 == 1

	def matrix_to_list(self, matrix: List[List[int]]) -> List[int]:
		result = []
		for i in range(len(matrix)):
			for j in range(len(matrix[i])):
				result.append(matrix[i][j])
		return result

	def snail_state(self) -> List[List[int]]:
		side = self.side if not self.side == 0 else len(self.source_state)
		matrix = [[0] * side for i in range(side)]
		digit, indentation = 1, 0
		for v in range(side // 2):
			for i in range(side - indentation):
				matrix[v][i + v] = digit
				digit += 1
			for i in range(v + 1, side - v):
				matrix[i][-v - 1] = digit
				digit += 1
			for i in range(v + 1, side - v):
				matrix[-v - 1][-i - 1] = digit
				digit += 1
			for i in range(v + 1, side - (v + 1)):
				matrix[-i - 1][v] = digit
				digit += 1
			indentation += 2
		matrix[side // 2][side // 2] = 0
		return matrix

	def get_state_from_file(self):
		matrix = []
		with open(os.path.join(config.STATES_DIR, self.file)) as f:
			for line in f:
				num_line = []
				matrix.append(num_line)
				nums = line.split()
				for num in nums:
					num_line.append(num)
		self.validate_matrix(matrix)
		print(matrix)
		return matrix

	def validate_matrix(self, matrix: List[List[str]]) -> None:
		nums = set()
		n_lines = len(matrix)
		for i in range(n_lines):
			if not n_lines == len(matrix[i]):
				raise NotValidMatrix('matrix not square')
			for j in range(len(matrix[i])):
				try:
					matrix[i][j] = int(matrix[i][j])
				except ValueError:
					raise NotValidMatrix('matrix have not numerical values')
				if matrix[i][j] in nums:
					raise NotValidMatrix('matrix have same elements')
				nums.add(matrix[i][j])
		if not 0 in nums:
			raise NotValidMatrix("matrix haven't got 0")

	def print_matrix(self):
		print("Source state")
		side = len(self.source_state)
		for i in range(side):
			for j in range(side):
				num = self.source_state[i][j]
				print(num, end='\t')
			print()
		print("\nFinal state")
		for i in range(side):
			for j in range(side):
				num = self.target_state[i][j]
				print(num, end='\t')
			print()


def start():
	try:
		a = StateGenerator(file='test')
		a.print_matrix()
	except NotValidMatrix as er:
		print(er)


if __name__ == "__main__":
	print(config.STATES_DIR)
	start()