from random import randint

class Algarismo:
	_digit: int

	def __init__(self, id: int) -> None:
		self._digit = id

	def print_number(self):
		print(self._digit, end="")

class AlgarismoFactory:
	def __init__(self):
		self.algarismos = {}

	def get_instance(self, id: int) -> Algarismo:
		if id in self.algarismos.keys():
			return self.algarismos[id]

		self.algarismos[id] = Algarismo(id)
		return self.algarismos[id]

class RandomNumberGenerator:
	digits: AlgarismoFactory

	def __init__(self):
		self.digits = AlgarismoFactory()

	def generate(self):
		for i in range(10):
			self.digits.get_instance(randint(0, 9)).print_number()

		print("")
		print(f"Number of instanciated classes: {len(self.digits.algarismos.keys())}")

def main():
	rng = RandomNumberGenerator()

	rng.generate()

if __name__ == "__main__":
	main()