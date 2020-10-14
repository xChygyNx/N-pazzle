from typing import Iterable, NamedTuple, Callable
from src.algorithm.vertex import *
from src.exceptions.exceptions import *
from copy import deepcopy


class Coordinate(NamedTuple):
	row: int
	column: int


def find_void(state: List[List[int]]) -> Coordinate:
	for i in range(len(state)):
		for j in range(len(state[i])):
			if state[i][j] == 0:
				return Coordinate(row=i, column=j)
	raise NotFoundVoid()


def variants_of_step(state: Vertex, target: List[List[int]],
                     heuristic: Callable[[List[List[int]], List[List[int]]], int]) -> Iterable[Vertex]:
	void = find_void(state.state)
	next_state = deepcopy(state.state)
	if void.row > 0:
		next_state[void.row][void.column], next_state[void.row - 1][void.column] =\
			next_state[void.row - 1][void.column], next_state[void.row][void.column]
		yield Vertex(state=next_state, parent=state.state, steps_from_init=state.steps_from_init + 1,
		             steps_to_target=heuristic(next_state, target))
	next_state = deepcopy(state.state)
	if void.row < (len(state.state) - 1):
		next_state[void.row][void.column], next_state[void.row + 1][void.column] = \
			next_state[void.row + 1][void.column], next_state[void.row][void.column]
		yield Vertex(state=next_state, parent=state.state, steps_from_init=state.steps_from_init + 1,
		             steps_to_target=heuristic(next_state, target))
	next_state = deepcopy(state.state)
	if void.column > 0:
		next_state[void.row][void.column], next_state[void.row][void.column - 1] =\
			next_state[void.row][void.column - 1], next_state[void.row][void.column]
		yield Vertex(state=next_state, parent=state.state, steps_from_init=state.steps_from_init + 1,
		             steps_to_target=heuristic(next_state, target))
	next_state = deepcopy(state.state)
	if void.column < (len(state.state[void.row]) - 1):
		next_state[void.row][void.column], next_state[void.row][void.column + 1] = \
			next_state[void.row][void.column + 1], next_state[void.row][void.column]
		yield Vertex(state=next_state, parent=state.state, steps_from_init=state.steps_from_init + 1,
		             steps_to_target=heuristic(next_state, target))
