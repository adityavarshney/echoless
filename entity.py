# Contains information regarding the Entity Class
# Entities refer to entities in language processed by the Google ML NLP platform.

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

	def avg_score(self):
		return self.score_sum / self.count

	# Compare entities by calculating their average scores
	def __lt__(self, other):
		return abs(self.avg_score()) > abs(other.avg_score())

	def __eq__(self, other):
		return abs(self.avg_score()) == abs(other.avg_score())