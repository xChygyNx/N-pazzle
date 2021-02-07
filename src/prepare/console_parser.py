import argparse


__all__ = ['ConsoleParser']


class ConsoleParser:
	@classmethod
	def get_argparse(cls) -> argparse.ArgumentParser:
		""" Возвращает парсер аргументов командной строки """
		parser = argparse.ArgumentParser(description='Parser for N-puzzle')
		parser.add_argument('--size', '-s',
							required=False,
							type=int,
							help='Size of puzzle')
		parser.add_argument('--init_file', '-if',
							required=False,
							type=str,
							help='File with start state (default start state generate randomly)')
		parser.add_argument('--unsolvable', '-u',
							required=False,
							action='store_true',
							default=False,
							help="Forces generation of a solvable puzzle. Overrides -unsolvable.")
		parser.add_argument('--heuristics', '-hr',
							required=False,
							type=str,
							default='md',
							choices=['md', 'lc', 'ct'],
							help='Choice of heuristic for search solution')
		parser.add_argument('--hungry',
							required=False,
							action='store_true',
							help='Hungry mode')
		parser.add_argument('--iterations', '-i',
							type=int,
							default=10000,
							help='Number of passes')
		parser.add_argument('--uninformed_search_strategy', '-uss',
							required=False,
							action='store_true',
							help='Search without heuristic, use breadth_first search')
		return parser
