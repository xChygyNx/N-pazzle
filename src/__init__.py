from typing import List, Any


__all__ = ['Vertex']


RED = '\033[31m'
WHITE = '\033[37m'


class Vertex:
	def __init__(self, *, state: List[List[int]], parent: Any = None, steps_from_init: int,
				steps_to_target: float, turn: str = None):
		self.parent = parent
		self.state = state
		self.steps_from_init = steps_from_init
		self.steps_to_target = steps_to_target
		self.potential_steps = steps_to_target + steps_from_init
		self.str_state = self.state_to_str()
		self.turn = turn

	def is_square(self) -> bool:
		row_count = len(self.state)
		for line in self.state:
			if not len(line) == row_count:
				return False
		return True

	def size_matrix(self):
		row_count = len(self.state)
		col_count = len(next(iter(self.state)))
		return row_count * col_count

	def check(self, other):
		if not isinstance(other, Vertex):
			raise NotImplementedError('Invalid types')
		if not (self.is_square() and other.is_square()):
			raise NotImplementedError('matrixes is not square')
		if not self.size_matrix() == other.size_matrix():
			raise NotImplementedError('matrixes different size')

	def __lt__(self, other):
		self.check(other)
		if self.potential_steps < other.potential_steps:
			return True
		return False

	def __gt__(self, other):
		self.check(other)
		if self.potential_steps > other.potential_steps:
			return True
		return False

	def __le__(self, other):
		self.check(other)
		if self.potential_steps <= other.potential_steps:
			return True
		return False

	def __ge__(self, other):
		self.check(other)
		if self.potential_steps >= other.potential_steps:
			return True
		return False

	def state_to_str(self):
		res = ''
		for line in self.state:
			for num in line:
				res += str(num)
		return res

	def __hash__(self):
		return hash(self.str_state)

	def __eq__(self, other):
		if self.__hash__() != other.__hash__():
			return False
		if not isinstance(self, other.__class__):
			return False
		if len(self.state) != len(other.state):
			return False
		for first, second in zip(self.state, other.state):
			if len(first) != len(second):
				return False
			for f_num, s_num in zip(first, second):
				if f_num != s_num:
					return False
		return True

	def print_state(self):
		for step, line in enumerate(self.state):
			for elem in line:
				if not elem:
					print(RED, end='')
				print(elem, end='\t')
				if not elem:
					print(WHITE, end='')
			print()

	def __str__(self):
		return str(self.steps_to_target)
