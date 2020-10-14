__all__ = ['NeedUsage', 'NotValidMatrix', 'ImpossibleSolute', 'NotFoundVoid']


class NotValidMatrix(Exception):
	def __init__(self, info: str):
		self.text = f"Not valid source matrix: {info}"

	def __str__(self):
		return self.text


class ImpossibleSolute(Exception):
	def __str__(self):
		return f"Impossible solute task with specified start and target state"


class NotFoundVoid(Exception):
	def __str__(self):
		return "State haven't got void"


class NeedUsage(Exception):
	def __init__(self):
		self.text = " For launch program need least one parameter:\n" \
		            "-sf - file with start state (need positive digit more 0)\n" \
		            "-tf - file with target state\n" \
		            "-s - side of start and target state"

	def __str__(self):
		return self.text
