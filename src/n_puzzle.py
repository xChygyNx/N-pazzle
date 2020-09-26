from src.prepare.state import NPuzzle
from src.prepare.console_parser import ConsoleParser
from src.exceptions.exceptions import *


if __name__ == '__main__':
	parser = ConsoleParser().get_argparse()
	args = parser.parse_args()
	try:
		print(args.side, args.start_file, args.target_file)
		states = NPuzzle(side=args.side, start_file=args.start_file, target_file=args.target_file)
		states.print_states()
	except (NotValidMatrix, ImpossibleSolute, NeedUsage) as exc:
		print(exc)