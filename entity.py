class Entity():
	def __init__(self, name, entity_type):
		self.name = name
		self.type = entity_type
		self.count = 0
		self.salience_sum = 0
		self.score_sum = 0
		self.magnitude_sum = 0

	def increment_count(self):
		self.count += 1

	def increment_salience(self, salience):
		self.salience_sum += salience

	def increment_score(self, score):
		self.score_sum += score

	def increment_magnitude(self, magnitude):
		self.magnitude_sum += magnitude

	def __lt__(self, other):
		return self.salience_sum > other.salience_sum

	def __eq__(self, other):
		return self.salience_sum == other.salience_sum