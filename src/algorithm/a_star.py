import heapq
from typing import List, Callable
from src.algorithm import *
from src import Vertex

__all__ = ['AlgorithmFactory', 'AStarAlgorithm', 'BFSAlgorithm']

WHITE = '\033[37m'


class Algorithm:
	def __init__(self, *, init_state: Vertex, target: List[List[int]], hungry_mode: bool):
		self.init_state = init_state
		self.target_state = target
		self.hungry_mode = hungry_mode
		self.opened = []
		self.closed = dict()

	def solute(self):
		raise NotImplementedError

	def get_from_closed(self, vertex: Vertex) -> Vertex:
		result = self.closed.get(vertex.str_state)
		return result

	def print_solution(self, state: Vertex) -> None:
		if state is None:
			return
		solution = []
		moves = []
		tmp = state
		while tmp is not None:
			solution.append(tmp)
			if tmp.turn is not None:
				moves.append(tmp.turn)
			tmp = tmp.parent
		solution.reverse()
		moves.reverse()
		print(WHITE)
		for step, elem in enumerate(solution):
			print(f'Step {step}')
			elem.print_state()
			print()
		print('Sequence of moves:')
		for move in moves:
			print(move, end=' ')
		print()


class AlgorithmFactory:
	def __init__(self, *, init_state: Vertex, target: List[List[int]],
				heuristic: Callable[[List[List[int]], List[List[int]]], int],
				hungry_mode: bool, uss: bool):
		self.init_state = init_state
		self.target_state = target
		self.heuristic = heuristic
		self.hungry_mode = hungry_mode
		self.uninformed_search_strategy = uss

	def get_algorithm(self) -> Algorithm:
		if self.uninformed_search_strategy:
			return BFSAlgorithm(self.init_state, self.target_state, self.hungry_mode)
		else:
			return AStarAlgorithm(self.init_state, self.target_state, self.heuristic, self.hungry_mode)


class AStarAlgorithm(Algorithm):
	def __init__(self, init_state: Vertex, target: List[List[int]],
				heuristic: Callable[[List[List[int]], List[List[int]]], int],
				hungry_mode: bool = False):
		super().__init__(init_state=init_state, target=target, hungry_mode=hungry_mode)
		self.heuristic = heuristic

	def get_from_opened(self, state: Vertex) -> Vertex:
		ind = self.opened.index(state)
		elem = self.opened[ind]
		return elem

	def solute(self) -> None:
		state = self.init_state
		heapq.heapify(self.opened)
		heapq.heappush(self.opened, state)
		while len(self.opened):
			state = heapq.heappop(self.opened)
			self.closed[state.str_state] = state
			if not self.heuristic(state.state, self.target_state):
				break
			for variant in variants_of_step(state, self.target_state, self.heuristic):
				if not (variant in self.closed.values() or variant in self.opened):
					heapq.heappush(self.opened, variant)
				elif variant in self.closed.values():
					if not self.hungry_mode:
						state_from_closed = self.get_from_closed(variant)
						if state_from_closed.steps_from_init > variant.steps_from_init:
							self.closed.pop(state_from_closed.str_state)
							heapq.heappush(self.opened, variant)
				else:
					state_from_opened = self.get_from_opened(variant)
					if variant.steps_from_init < state_from_opened.steps_from_init:
						self.opened.remove(state_from_opened)
						heapq.heappush(self.opened, variant)
		self.print_solution(state)
		print()
		print(f'steps from init = {state.steps_from_init}')


class BFSAlgorithm(Algorithm):
	def __init__(self, init_state: Vertex, target: List[List[int]],
				hungry_mode: bool = False):
		super().__init__(init_state=init_state, target=target, hungry_mode=hungry_mode)

	def solute(self):
		state = self.init_state
		self.opened.append(state)
		while self.opened:
			state = self.opened.pop(0)
			self.closed[state.str_state] = state
			if state.state == self.target_state:
				break
			for variant in variants_of_step(state, self.target_state):
				if not (variant in self.closed.values() or variant in self.opened):
					self.opened.append(variant)
				elif variant in self.closed.values():
					continue
		self.print_solution(state)
		print()
		print(f'steps from init = {state.steps_from_init}')
