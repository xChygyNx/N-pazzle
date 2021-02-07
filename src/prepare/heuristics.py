from typing import List, NamedTuple, Union, Any
import math

__all__ = ['manhattan_distance', 'linear_conflict', 'corner_tiles']


class Location(NamedTuple):
	x: int
	y: int


def find_target_pos(num: int, state: List[List[int]]) -> Union[Location, None]:
	for i in range (len(state)):
		for j in range(len(state[i])):
			if state[i][j] == num:
				return Location(x=i, y=j)
	return None


def manhattan_distance(state: List[List[int]], target: List[List[int]]) -> int:
	res = 0
	for i in range(len(state)):
		for j in range(len(state[i])):
			value = state[i][j]
			target_pos = find_target_pos(value, target)
			res += math.fabs(i - target_pos.x) + math.fabs(j - target_pos.y)
	return res


def count_conflicts(state_line: List[int], target_line: List[int]) -> int:
	res = 0
	for i in range(len(state_line) - 1):
		for j in range(i + 1, len(state_line)):
			try:
				first_num_pos = target_line.index(state_line[i])
				second_num_pos = target_line.index(state_line[j])
			except ValueError:
				continue
			if first_num_pos > second_num_pos:
				res += 2
	return res


def transpose_matrix(matrix: List[List[Any]]) -> List[List[Any]]:
	size = len(matrix)
	res = [[0] * size for _ in range(size)]
	for i in range(size):
		for j in range(size):
			res[i][j] = matrix[j][i]
	return res


def linear_conflict(state: List[List[int]], target: List[List[int]]) -> int:
	res = manhattan_distance(state, target)
	for lines in zip(state, target):
		res += count_conflicts(lines[0], lines[1])
	transposed_state = transpose_matrix(state)
	transposed_target = transpose_matrix(target)
	for lines in zip(transposed_state, transposed_target):
		res += count_conflicts(lines[0], lines[1])
	return res


def corner_tiles(state: List[List[int]], target: List[List[int]]) -> int:
	res = linear_conflict(state, target)
	size = len(state) - 1
	corners = [(0, 0), (0, size), (size, 0), (size, size)]
	transpose_target = transpose_matrix(target)
	for i, j in corners:
		if not state[i][j] == target[i][j]:
			if not (state[i][j] in target[i]) or (state[i][j] in transpose_target[j]):
				res += 2
	return res
