import os
from random import choice
from typing import List
import src.config as config
from src.prepare.validating_states import ValidateState


__all__ = ['RandomInitStateGenerator', 'SnailState', 'StateFromFile']


class RandomInitStateGenerator:
	def __init__(self, side: int):
		self.side = side

	def get_state(self) -> List[List[int]]:
		matrix = [[0] * self.side for _ in range(self.side)]
		plates = [x for x in range(self.side ** 2)]

		for i in range(self.side):
			for j in range(self.side):
				num = choice(plates)
				matrix[i][j] = num
				plates.remove(num)
		return matrix


class SnailState:
	def __init__(self, side: int):
		self.side = side

	def get_state(self) -> List[List[int]]:
		side = self.side
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
		matrix[side // 2][(side - 1) // 2] = 0
		return matrix


class StateFromFile:
	def __init__(self, file: str):
		self.file = file

	def get_state(self):
		matrix = []
		with open(os.path.join(config.STATES_DIR, self.file)) as f:
			for line in f:
				nums_line = []
				matrix.append(nums_line)
				nums = line.split()
				for num in nums:
					nums_line.append(num)
		ValidateState(matrix, self.file)
		return matrix
