class NotValidMatrix(Exception):
	def __init__(self, info: str):
		self.text = f"Not valid source matrix: {info}"

	def __str__(self):
		return self.text
