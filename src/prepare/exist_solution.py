from typing import List, Union, Tuple
from src.prepare.format_state import FormatState
from copy import deepcopy


__all__ = ['ExistSolution']


class ExistSolution:
	def __init__(self, source_state: Union[List[List[int]]]):
		self.source_state = source_state

	def	exist_solution(self) -> bool:
		tmp_state = self.zero_in_corner(deepcopy(self.source_state))
		src_line_with_void = self.define_line_with_void(tmp_state)
		src_list = FormatState().matrix_to_list(tmp_state)
		src_inversion = self.count_inversions(src_list)
		# print(src_inversion + src_line_with_void, dst_inversion + dst_line_with_void)
		return (src_line_with_void + src_inversion) % 2 == 0

	def define_line_with_void(self, state: List[List[int]]) -> int:
		line_with_void = 0
		for i in range(len(state)):
			for j in range(len(state[i])):
				if state[i][j] == 0:
					line_with_void = 1 + i
		return line_with_void

	def count_inversions(self, _list: List[int]) -> int:
		inversions = 0
		for i in range(len(_list)):
			for j in range(i + 1, len(_list)):
				if not _list[j] == 0:
					if _list[i] > _list[j]:
						inversions += 1
		return inversions

	def zero_in_corner(self, state: List[List[int]]) -> List[List[int]]:
		size = len(state)
		x, y = self.zero_pos(state)
		for i in range(y, size - 1):
			state[x][i], state[x][i + 1] = state[x][i + 1], state[x][i]
		for j in range(x, size - 1):
			state[j][size - 1], state[j + 1][size - 1] = state[j + 1][size - 1], state[j][size - 1]
		return state

	def zero_pos(self, state: List[List[int]]) -> Tuple[int, int]:
		size = len(state)
		for x in range(size):
			if 0 in state[x]:
				break
		y = state[x].index(0)
		return x, y



