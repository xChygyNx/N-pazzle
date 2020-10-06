import argparse


class ConsoleParser:
	@classmethod
	def get_argparse(cls) -> argparse.ArgumentParser:
		""" Возвращает парсер аргументов командной строки """
		parser = argparse.ArgumentParser(description='Parser for N-puzzle')
		parser.add_argument('--side', '-s',
		                    required=False,
		                    type=int,
		                    choices=range(0, 30),
		                    help='Side of randomly generated state')
		parser.add_argument('--start_file', '-sf',
		                    required=False,
		                    type=str,
		                    default=None,
		                    help='File which stored start state')
		parser.add_argument('--target_file', '-tf',
		                    required=False,
		                    default=None,
		                    help='File which stored target state')
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

		return parser
