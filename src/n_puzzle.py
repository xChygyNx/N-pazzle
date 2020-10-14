from src.prepare.state import NPuzzle
from src.prepare.console_parser import ConsoleParser
from src.exceptions.exceptions import *
from src.prepare.heuristics import *
from src.prepare.generating_state import *
from src.algorithm import *
from src.algorithm.trouble_shooter import *


heuristics = {
	'md': manhattan_distance,
	'lc': linear_conflict,
	'ct': corner_tiles
}

if __name__ == '__main__':
	parser = ConsoleParser().get_argparse()
	args = parser.parse_args()
	# try:
	# 	states = NPuzzle(side=args.side, start_file=args.start_file, target_file=args.target_file)
	# 	states.print_states()
	# 	print(args.hungry)
	# except (NotValidMatrix, ImpossibleSolute, NeedUsage) as exc:
	# 	print(exc)
	print(args.heuristics)
	init_state = StateFromFile('file.txt').get_state()
	target_state = SnailState(args.side).get_state()
	heuristic = heuristics.get(args.heuristics)
	init_vertex = Vertex(state=init_state, steps_from_init=0,
	                     steps_to_target=heuristic(init_state, target_state))
	n_puzzle = TroubleShooter(init_state=init_vertex, target=target_state, heuristic=heuristic)
	n_puzzle.solute()


