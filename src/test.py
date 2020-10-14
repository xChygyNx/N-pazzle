from queue import PriorityQueue
from src.algorithm.vertex import Vertex
class A:
	def __init__(self, num, matrix):
		self.num = num
		self.matrix = matrix

	# def __hash__(self):
	# 	return self.num * self.matrix

	def __str__(self):
		return str(self.__hash__())

	def is_square(self)->bool:
		row_count = len(self.matrix)
		for line in self.matrix:
			if not len(line) == row_count:
				return False
		return True

	def size_matrix(self):
		row_count = len(self.matrix)
		col_count = len(next(iter(self.matrix)))
		return row_count * col_count

	def check(self, other):
		if not isinstance(other, A):
			raise NotImplemented('Invalid types')
		if not self.is_square() and other.is_square():
			raise NotImplemented('matrixes is not square')
		if not self.size_matrix() == other.size_matrix():
			raise NotImplemented('matrixes different size')

	def __lt__(self, other):
		self.check(other)
		for lines in zip(self.matrix, other.matrix):
			for nums in zip(lines[0], lines[1]):
				if nums[1] <= nums[0]:
					return False
		return True


class B:
	def __init__(self, num: int):
		self.num = num

	def __hash__(self):
		return self.num % 10

	def __eq__(self, other):
		if other.__hash__() == self.__hash__():
			return True
		return False


class C:
	def __init__(self, num):
		self.num = num

	def __hash__(self):
		return self.num

a = Vertex(state=[[2, 20], [4, 83]], steps_from_init=7)
b = Vertex(state=[[2, 20], [48, 3]], parent=a, steps_from_init=7)
c = Vertex(state=[[2, 8], [11, 2]], parent=a, steps_from_init=7)
queue = PriorityQueue()
queue.put((a.potential_steps(), a))
queue.put((b.potential_steps(), b))
queue.put((c.potential_steps(), c))
while not queue.empty():
	print(queue.get()[1].state)
print(a<b)
a.check(b)
print(a.state_to_str())
print('a' * 6)
res = [[0] * 5 for _ in range(5)]
res[4][1] = 9
print(res)
ex1 = B(3)
ex2 = B(13)
ex3 = C(3)
mn = {ex1}
print(ex2 in mn)
print(ex1 == ex3)
test = [9, 7, 0, 56, 4, 0]
print(min(test))



