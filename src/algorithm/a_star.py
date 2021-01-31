from typing import List, Callable, Set, Dict, Optional
from queue import PriorityQueue
from src.algorithm import *
from src.prepare.heuristics import *
from copy import deepcopy
from src import Vertex
import timeit
import heapq

import cProfile

__all__ = ['Algorithm']

WHITE = '\033[37m'


class Algorithm:
	def __init__(self, *, init_state: Vertex, target: List[List[int]],
	             heuristic: Callable[[List[List[int]], List[List[int]]], int],
				 hungry_mode: bool = False):
		self.opened = PriorityQueue()
		self.closed = dict()
		self.init_state = init_state
		self.target_state = target
		self.heuristic = heuristic
		self.hungry_mode = hungry_mode


	def get_from_closed(self, vertex: Vertex) -> Vertex:
		result = self.closed.get(vertex.str_state)
		return result

	# def get_from_opened(self, state: Vertex) -> Vertex:
	# 	ind = self.opened.index(state)
	# 	elem = self.opened[ind]
	# 	return elem

	def solute(self) -> None:
		state = self.init_state
		self.opened.put(state)
		while not self.opened.empty():
			state = self.opened.get()
			self.closed[state.str_state] = state
			if not self.heuristic(state.state, self.target_state):
				break
			for variant in variants_of_step(state, self.target_state, self.heuristic):
				if variant not in self.closed.values():
					self.opened.put(variant)
				elif variant in self.closed.values():
					if not self.hungry_mode:
						state_from_closed = self.get_from_closed(variant)
						if state_from_closed.steps_from_init > variant.steps_from_init:
							self.closed.pop(state_from_closed.str_state)
							self.opened.put(variant)
				# else:
				# 	state_from_opened = self.get_from_opened(variant)
				# 	if variant.steps_from_init < state_from_opened.steps_from_init:
				# 		self.opened.remove(state_from_opened)
				# 		heapq.heappush(self.opened, variant)
		self.print_solution(state)
		print(f'steps from init = {state.steps_from_init}')


	def print_solution(self, state: Vertex) -> None:
		if state is None:
			return
		solution = []
		tmp = state
		while tmp is not None:
			solution.append(tmp)
			tmp = tmp.parent
		solution.reverse()
		print(WHITE)
		for step, elem in enumerate(solution):
			print(f'Step {step}')
			elem.print_state()
			print()
		# print(f'Total opened: {len(self.opened)}')
		print(f'Total closed: {len(self.closed)}')

