from typing import List, Callable, Set
from queue import PriorityQueue
from src.algorithm import *
from src.prepare.heuristics import *


class TroubleShooter:
	def __init__(self, *, init_state: Vertex, target: List[List[int]],
	             heuristic: Callable[[List[List[int]], List[List[int]]], int]):
		self.opened = set()
		# self.open_count = dict()
		self.closed = set()
		self.init_state = init_state
		self.target_state = target
		self.heuristic = heuristic

	# def put_in_open(self, state: Vertex) -> None:
	# 	self.open.put((state.potential_steps(), state))
	# 	self.open_count[state] = self.open_count.get(state, 0) + 1

	def get_from_set(self, storage: Set[Vertex], vertex: Vertex) -> Vertex:
		tmp = storage.intersection({vertex})
		result = tmp.pop()
		storage.remove(result)
		return result

	def get_from_opened(self) -> Vertex:
		elem = min(self.opened)
		self.opened.remove(elem)
		return elem

	def solute(self):
		success = False
		state = self.init_state
		self.opened.add(state)
		while not len(self.opened):
			state = self.get_from_opened()
			self.closed.add(state)
			self.closed.add(state)
			if not self.heuristic(state.state, self.target_state):
				success = True
				break
			for variant in variants_of_step(state, self.target_state, self.heuristic):
				if variant not in self.opened and variant not in self.closed:
					self.opened.add(variant)
				elif variant in self.closed:
					state_from_closed = self.get_from_set(self.closed, variant)
					if state_from_closed.steps_from_init > variant.steps_from_init:
						state_from_closed.steps_from_init = variant.steps_from_init
					self.closed.add(state_from_closed)
				# else:
			break
		if success:
			print('Congratulate')
		else:
			print('Ouch')


# if __name__ == '__main__':
# 	a = Vertex(state=[[1, 2, 3], [4, 5, 6], [7, 0, 8]], steps_from_init=5, steps_to_target=7)
# 	b = Vertex(state=[[1, 2, 3], [4, 5, 6], [7, 0, 8]], steps_from_init=3, steps_to_target=7)
# # 	c = Vertex(state=[[8, 7, 2], [3, 0, 1], [4, 6, 5]], steps_from_init=3)
# # 	d = Vertex(state=[[8, 7, 2], [3, 0, 1], [6, 4, 5]], steps_from_init=3)
# # 	sol = TroubleShooter(init_state=b, target=[[1, 2, 3], [4, 5, 6], [7, 8, 0]], heuristic=manhattan_distance)
# # 	a.print_state()
# # 	print()
# # 	sol.solute()
# 	# s = {6, 9, 1, 16, 90, 3}
# 	# sVertex = {a, b, c, d}
# 	# for v in sorted(sVertex):
# 	# 	v.print_state()
# 	# 	print(f'distance = {v.steps_from_init}')
# 	# 	print(f'potential steps = {v.potential_steps()}')
# 	# 	print()
# 	s = {a}
# 	print(len(s))
# 	tmp = s.intersection({b})
# 	d = tmp.pop()
# 	print(len(s))
# 	s.remove(d)
# 	print(len(s))
# 	print(d.steps_from_init)
