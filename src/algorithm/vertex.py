from typing import List, Any

class Vertex:
	def __init__(self, *, state: List[List[int]], parent: Any = None, steps_to_init: int):
		self.parent = parent
		self.state = state
		self.steps_to_init = steps_to_init
		self.steps_to_target = 10

	def is_square(self)->bool:
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
		for lines in zip(self.state, other.state):
			for nums in zip(lines[0], lines[1]):
				if nums[0] != nums[1]:
					if nums[1] < nums[0]:
						return False
					else:
						return True
		return False

	def __gt__(self, other):
		self.check(other)
		for lines in zip(self.state, other.state):
			for nums in zip(lines[0], lines[1]):
				if nums[0] != nums[1]:
					if nums[1] > nums[0]:
						return False
					else:
						return True
		return False

	def __le__(self, other):
		self.check(other)
		if self.__lt__(other) or self.__eq__(other):
			return True
		return False

	def __ge__(self, other):
		self.check(other)
		if self.__gt__(other) or self.__eq__(other):
			return True
		return False

	def __eq__(self, other):
		self.check(other)
		for lines in zip(self.state, other.state):
			for nums in zip(lines[0], lines[1]):
				if nums[0] != nums[1]:
					return False
		return True

	def state_to_str(self):
		res = ''
		for line in self.state:
			for num in line:
				res += str(num)
		return res

	def potential_steps(self):
		return self.steps_to_init + self.steps_to_target


	def __hash__(self):
		return hash(self.state_to_str())



if __name__ == '__main__':
	a = Vertex(state=[[2, 2], [4, 6]], steps_to_init=0)
	b = Vertex(state=[[2, 6], [4, 2]], parent=a, steps_to_init=1)
	print(b)
	print(a == b.parent)
	res = {a: 15,
	     b: 18}
	for rec in res:
		print(rec)
	print()
	res[Vertex(state=[[2, 6], [4, 2]], parent=a, steps_to_init=1)] = 20
	for rec in res:
		print(rec)

