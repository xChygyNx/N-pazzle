from typing import List
from src.exceptions.exceptions import *


class ValidateState:
	def __init__(self, state: List[List[str]], file: str):
		self.state = state
		self.state_size = len(self.state)
		self.file = file

	def is_square(self) -> None:
		for line in self.state:
			if not len(line) == self.state_size:
				raise NotValidMatrix(f'Invalid file {self.file}: state not square')

	def is_only_numeric_value(self) -> None:
		for i in range(self.state_size):
			for j in range(len(self.state[i])):
				try:
					self.state[i][j] = int(self.state[i][j])
				except ValueError:
					raise NotValidMatrix(f'Invalid file {self.file}: state have not numerical value')

	def is_unique_values(self) -> None:
		meeting_nums = set()
		for i in range(self.state_size):
			for j in range(len(self.state[i])):
				if self.state[i][j] in meeting_nums:
					raise NotValidMatrix(f'Invalid file {self.file}: state have same elements')
				meeting_nums.add(self.state[i][j])

	def is_have_void(self) -> None:
		for i in range(self.state_size):
			for j in range(len(self.state[i])):
				if self.state[i][j] == 0:
					return
		raise NotValidMatrix(f"Invalid file {self.file}: state haven't got 0")

	def validate_state(self) -> None:
		self.is_square()
		self.is_only_numeric_value()
		self.is_unique_values()
		self.is_have_void()
