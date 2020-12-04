from typing import List, Callable, Set, Dict
from queue import PriorityQueue
from src.algorithm import *
from src.prepare.heuristics import *
from copy import deepcopy
import timeit
import heapq





class TroubleShooter:
	def __init__(self, *, init_state: Vertex, target: List[List[int]],
	             heuristic: Callable[[List[List[int]], List[List[int]]], int]):
		self.opened = []
		self.closed = dict()
		self.init_state = init_state
		self.target_state = target
		self.heuristic = heuristic


	def get_from_closed(self, vertex: Vertex) -> Vertex:
		result = self.closed.get(vertex.state_to_str())
		return result

	def get_from_opened(self, state: Vertex) -> Vertex:
		ind = self.opened.index(state)
		elem = self.opened[ind]
		return elem

	def solute(self):
		success = False
		state = self.init_state
		heapq.heapify(self.opened)
		heapq.heappush(self.opened, state)
		while len(self.opened):
			state = heapq.heappop(self.opened)
			self.closed[state.state_to_str()] = state
			if not self.heuristic(state.state, self.target_state):
				success = True
				break
			for variant in variants_of_step(state, self.target_state, self.heuristic):
				if variant not in self.closed.values() and variant not in self.opened:
					heapq.heappush(self.opened, variant)
				elif variant in self.closed.values():
					state_from_closed = self.get_from_closed(variant)
					if state_from_closed.steps_from_init > variant.steps_from_init:
						self.closed.pop(state_from_closed.state_to_str())
						heapq.heappush(self.opened, variant)
				else:
					state_from_opened = self.get_from_opened(variant)
					if variant.steps_from_init < state_from_opened.steps_from_init:
						self.opened.remove(state_from_opened)
						heapq.heappush(self.opened, variant)
		if success:
			print('Congratulate')
			self.print_solution(state)
			print(f'steps from init = {state.steps_from_init}')
		else:
			print('Ouch')

	def print_solution(self, state: Vertex) -> None:
		solution = []
		tmp = state
		while tmp is not None:
			solution.append(tmp)
			tmp = tmp.parent
		solution.reverse()
		for elem in solution:
			elem.print_state()
			print()


if __name__ == '__main__':
	# a = Vertex(state=[[6, 14, 1, 2], [7, 3, 4, 5], [11, 15, 12, 13], [0, 8, 9, 10]], steps_from_init=0, steps_to_target=10)
	# sol = TroubleShooter(init_state=a, target=[[1, 2, 3, 4], [12, 13, 14, 5], [11, 0, 15, 6], [10, 9, 8, 7]], heuristic=manhattan_distance)
	a = Vertex(state=[[0, 2, 1], [8, 7, 4], [3, 5, 6]], steps_from_init=0, steps_to_target=16.0)
	sol = TroubleShooter(init_state=a, target=[[1, 2, 3], [8, 0, 4], [7, 6, 5]], heuristic=manhattan_distance)
	elapsed_time = timeit.timeit(sol.solute, number=1)
	print(f'time = {elapsed_time}')
	# sol.solute()
