from typing import List, Union
from src.format_state import FormatState


class ExistSolution:
	def __init__(self, source_state: Union[List[List[int]]],
	             dst_state: Union[List[List[int]]]):
		self.source_state = source_state
		self.dst_state = dst_state

	def	exist_solution(self) -> bool:
		if not len(self.source_state) == len(self.dst_state):
			return False
		src_line_with_void = self.define_line_with_void(self.source_state)
		dst_line_with_void = self.define_line_with_void(self.dst_state)
		src_list = FormatState().matrix_to_list(self.source_state)
		dst_list = FormatState().matrix_to_list(self.dst_state)
		src_inversion = self.count_inversions(src_list)
		dst_inversion = self.count_inversions(dst_list)
		return (src_inversion + src_line_with_void) % 2 == (dst_inversion + dst_line_with_void) % 2

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
			if not _list[i] == 0:
				for j in range(i + 1, len(_list)):
					if _list[i] > _list[j]:
						inversions += 1
		return inversions


