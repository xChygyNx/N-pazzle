import os
from random import choice
from typing import List
import src.config.config as config
from src.prepare.validating_states import ValidateState
from src.exceptions.exceptions import *
from src.prepare.exist_solution import *


__all__ = ['InitState', 'TargetState']


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

	def get_state(self) -> List[List[int]]:
		matrix = []
		with open(os.path.join(config.STATES_DIR, self.file)) as f:
			for line in f:
				if line.startswith('#'):
					continue
				else:
					size_state = self.get_state_size(line)
					break
			for line in f:
				if line.startswith('#'):
					continue
				nums_line = self.get_nums_line(line)
				matrix.append(nums_line)
		ValidateState(matrix, size_state, self.file).validate_state()
		return matrix

	def get_state_size(self, line: str) -> int:
		try:
			state_size = int(line)
		except ValueError:
			raise InvalidStateSize
		if state_size < 1:
			raise InvalidStateSize
		return state_size

	def get_nums_line(self, line: str) -> List[int]:
		split_str = line.split()
		res = []
		for elem in split_str:
			try:
				res.append(int(elem))
			except ValueError:
				raise InvalidNumInState(elem)
		return res


class InitState:
	def __init__(self, args):
		self.args = args

	def get_state(self) -> List[List[int]]:
		if not (self.args.init_file or self.args.size):
			raise NeedUsage
		elif self.args.init_file:
			state = StateFromFile(self.args.init_file).get_state()
			if not ExistSolution(state).exist_solution():
				raise ImpossibleSolute
		else:
			if self.args.size < 1:
				raise InvalidStateSize
			exist_solution = False
			while not exist_solution:
				state = RandomInitStateGenerator(self.args.size).get_state()
				exist_solution = ExistSolution(state).exist_solution()
		return state


class TargetState:
	def __init__(self, args, init_state: List[List[int]]):
		self.args = args
		self.init_state = init_state

	def get_state(self) -> List[List[int]]:
		size = len(self.init_state)
		if self.args.size and self.args.size < 3:
			raise InvalidStateSize
		state = SnailState(size).get_state()
		return state
