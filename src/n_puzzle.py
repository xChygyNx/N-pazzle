from src import *
from src.prepare.console_parser import ConsoleParser
from src.exceptions.exceptions import *
from src.prepare.heuristics import *
from src.prepare.generating_state import *
from src.algorithm.a_star import *
import timeit
import cProfile


heuristics = {
	'md': manhattan_distance,
	'lc': linear_conflict,
	'ct': corner_tiles
}

if __name__ == '__main__':
	parser = ConsoleParser().get_argparse()
	args = parser.parse_args()
	try:
		init_state = InitState(args).get_state()
		target_state = TargetState(args, init_state).get_state()
	except (NeedUsage, ImpossibleSolute, InvalidStateSize, InvalidNumInState) as exc:
		print(exc)
		exit()
	heuristic = heuristics.get(args.heuristics)
	step_to_target = heuristic(init_state, target_state)
	init_vertex = Vertex(state=init_state, steps_from_init=0,
	                     steps_to_target=step_to_target)
	n_puzzle = Algorithm(init_state=init_vertex, target=target_state,
						heuristic=heuristic, hungry_mode=args.hungry)
	# n_puzzle.solute()
	time = timeit.timeit(n_puzzle.solute, number=1)
	print(f'time = {time}')
	# cProfile.run('n_puzzle.solute()')


