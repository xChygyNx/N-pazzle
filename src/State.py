from typing import List
from src.generating_state import *
from src.exceptions.exceptions import *
from src.exist_solution import ExistSolution
from src.validating_states import ValidateState
from src.console_parser import ConsoleParser


class NPuzzle:
	def __init__(self, *, side: int = 0, start_file: str = None, target_file: str = None):
		self.side = side
		self.start_file = start_file
		self.target_file = target_file
		self.target_state = self.create_target_state()
		self.init_state = self.create_init_state()

	def create_init_state(self) -> List[List[int]]:
		if self.start_file is not None:
			state = StateFromFile(self.start_file).get_state()
			ValidateState(state, self.start_file)
			if not ExistSolution(state, self.target_state).exist_solution():
				raise ImpossibleSolute()
		else:
			exist_solution = False
			while not exist_solution:
				state = RandomInitStateGenerator(self.side).get_state()
				exist_solution = ExistSolution(state, self.target_state).exist_solution()
		return state

	def create_target_state(self) -> List[List[int]]:
		if self.target_file is not None:
			state = StateFromFile(self.target_file).get_state()
			ValidateState(state, self.target_file)
			self.side = len(state)
			return state
		elif not self.side == 0:
			return SnailState(self.side).get_state()
		elif self.start_file is not None:
			init_state = StateFromFile(self.start_file).get_state()
			ValidateState(init_state, self.start_file)
			return SnailState(len(init_state)).get_state()
		else:
			raise NeedUsage()

	def print_state(self):
		print("Source state")
		side = len(self.init_state)
		for i in range(side):
			for j in range(side):
				num = self.init_state[i][j]
				print(num, end='\t')
			print()
		print("\nFinal state")
		for i in range(side):
			for j in range(side):
				num = self.target_state[i][j]
				print(num, end='\t')
			print()


parser = ConsoleParser.get_argparse()
args = parser.parse_args()
try:
	npzl = NPuzzle(side=args.side, start_file=args.start_file, target_file=args.target_file)
	npzl.print_state()
except Exception as exc:
	print(exc)

