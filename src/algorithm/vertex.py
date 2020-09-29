from typing import List, Any

class Vertex:
	def __init__(self, *, state: List[List[int]], parent: Any = None, steps_to_init: int):
		self.parent = parent
		self.state = state
		self.steps_to_init = steps_to_init
		self.steps_to_target = 78


a = Vertex(state=[[2, 2], [4, 6]], steps_to_init=0)
b = Vertex(state=[[2, 6], [4, 2]], parent=a, steps_to_init=1)
print(b)
print(a == b.parent)
res = {a: 15,
     b: 18}
for rec in res:
	print(rec)
print()
res[Vertex(state=[[2, 6], [4, 2]], parent=a, steps_to_init=1)] = 20
for rec in res:
	print(rec)

