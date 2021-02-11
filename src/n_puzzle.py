from src import *
from src.prepare.console_parser import ConsoleParser
from src.exceptions.exceptions import *
from src.prepare.heuristics import *
from src.prepare.generating_state import *
from src.algorithm.a_star import *
import timeit


heuristics = {
	'md': manhattan_distance,
	'lc': linear_conflict,
	'ct': corner_tiles,
	'none': None
}

if __name__ == '__main__':
	parser = ConsoleParser().get_argparse()
	args = parser.parse_args()
	try:
		init_state = InitState(args).get_state()
		target_state = SnailState(init_state).get_state()
	except (NotValidMatrix, NeedUsage, ImpossibleSolute, InvalidStateSize, InvalidNumInState, FileNotFoundError) as exc:
		print(exc)
		exit()
	heuristic = heuristics.get(args.heuristics)
	step_to_target = heuristic(init_state, target_state)
	init_vertex = Vertex(state=init_state, steps_from_init=0,
						steps_to_target=step_to_target)
	n_puzzle = AlgorithmFactory(init_state=init_vertex, target=target_state,
						heuristic=heuristic, hungry_mode=args.hungry,
						uss=args.uninformed_search_strategy).get_algorithm()
	time = timeit.timeit(n_puzzle.solute, number=1)
	print(f'time complexity = {len(n_puzzle.closed)}')
	print(f'size complexity = {len(n_puzzle.opened) + len(n_puzzle.closed)}')
	print(f'time = {time}')


