from typing import List, Any, Callable
import random


RED = '\033[31m'
WHITE = '\033[37m'


class Vertex:
	def __init__(self, *, state: List[List[int]], parent: Any = None, steps_from_init: int,
	             steps_to_target: float):
		self.parent = parent
		self.state = state
		self.steps_from_init = steps_from_init
		self.steps_to_target = steps_to_target

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
		if not self.__eq__(other):
			if other.steps_to_target < self.steps_to_target:
				return False
			else:
				return True
		return False

	def __gt__(self, other):
		self.check(other)
		if not self.__eq__(other):
			if other.steps_to_target > self.steps_to_target:
				return False
			else:
				return True
		return False

	def __le__(self, other):
		self.check(other)
		if not self.__eq__(other):
			if other.steps_to_target <= self.steps_to_target:
				return False
			else:
				return True
		return False

	def __ge__(self, other):
		self.check(other)
		if not self.__eq__(other):
			if other.steps_to_target >= self.steps_to_target:
				return False
			else:
				return True
		return False

	def state_to_str(self):
		res = ''
		for line in self.state:
			for num in line:
				res += str(num)
		return res

	def potential_steps(self):
		return self.steps_from_init + self.steps_to_target

	def __hash__(self):
		return hash(self.state_to_str())

	def __eq__(self, other):
		if isinstance(self, other.__class__) and self.__hash__() == other.__hash__():
			return True
		return False

	def print_state(self):
		for line in self.state:
			for elem in line:
				if not elem:
					print(RED, end='')
				print(elem, end='\t')
				if not elem:
					print(WHITE, end='')
			print()


# if __name__ == '__main__':
# 	a = Vertex(state=[[2, 2], [4, 6]], steps_from_init=-43)
# 	b = Vertex(state=[[2, 4], [4, 6]], parent=a, steps_from_init=1)
# 	c = Vertex(state=[[2, 2], [4, 6]], parent=a, steps_from_init=1)
# 	mn = {c}
# 	print(a in mn)
# 	tmp = {a}.intersection(mn)
# 	d = tmp.pop()
# 	a.steps_from_init = 66
# 	print(d.parent.steps_from_init)
#
# 	# print(d.steps_from_init)


