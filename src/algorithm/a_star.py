from typing import List, Callable, Set, Dict, Optional
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
		self.opened = []
		self.closed = dict()
		self.init_state = init_state
		self.target_state = target
		self.heuristic = heuristic
		self.hungry_mode = hungry_mode


	def get_from_closed(self, vertex: Vertex) -> Vertex:
		result = self.closed.get(vertex.state_to_str())
		return result

	def get_from_opened(self, state: Vertex) -> Vertex:
		ind = self.opened.index(state)
		elem = self.opened[ind]
		return elem

	def solute(self) -> None:
		if not self.hungry_mode:
			finish_node = self.well_fed_solute()
		else:
			finish_node = self.hungry_mode_solute()
		self.print_solution(finish_node)
		print(f'steps from init = {finish_node.steps_from_init}')

	def hungry_mode_solute(self) -> Optional[Vertex]:
		success = False
		state = self.init_state
		closed_states = set()
		while not success:
			if not self.heuristic(state.state, self.target_state):
				success = True
				continue
			state = next_step(state, self.target_state, self.heuristic, closed_states)
		print(f'steps to target = {state.steps_to_target}')
		print(f'len closed_states {len(closed_states)}')
		return state


	def well_fed_solute(self) -> Optional[Vertex]:
		success = False
		state = self.init_state
		heapq.heapify(self.opened)
		heapq.heappush(self.opened, state)
		i=0
		while len(self.opened):
			# print(i)
			# i += 1
			state = heapq.heappop(self.opened)
			# print(f'steps to target = {state.steps_to_target}')
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
			return state
		else:
			print('Ouch')

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

