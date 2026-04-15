from abc import abstractmethod, ABCMeta

class Beverage(metaclass=ABCMeta):
	additionals = []

	@abstractmethod
	def display_beverage(self) -> None:
		...

class Expresso(Beverage):
	def display_beverage(self) -> None:
		print(f"Expresso with {self.additionals}.")

class Capuccino(Beverage):
	def display_beverage(self) -> None:
		print(f"Capuccino with {self.additionals}")

class Tea(Beverage):
	def display_beverage(self) -> None:
		print(f"Tea with {self.additionals}")

class BeverageDecorator(Beverage):
	def __init__(self, bev: Beverage):
		self.bev = bev

	def display_beverage(self) -> None:
		self.bev.display_beverage()

class MilkAdder(BeverageDecorator):
	def __init__(self, bev: Beverage):
		super().__init__(bev)
		if "Milk" not in super().additionals:
			super().additionals.append("Milk")

	def display_beverage(self) -> None:
		super().display_beverage()

class ChantillyAdder(BeverageDecorator):
	def __init__(self, bev: Beverage):
		super().__init__(bev)
		if "Chantilly" not in super().additionals:
			super().additionals.append("Chantilly")

	def display_beverage(self) -> None:
		super().display_beverage()

class ChocolateAdder(BeverageDecorator):
	def __init__(self, bev: Beverage):
		super().__init__(bev)
		if "Chocolate" not in super().additionals:
			super().additionals.append("Chocolate")

	def display_beverage(self) -> None:
		super().display_beverage()

class CinnamonAdder(BeverageDecorator):
	def __init__(self, bev: Beverage):
		super().__init__(bev)
		if "Cinnamon" not in super().additionals:
			super().additionals.append("Cinnamon")

	def display_beverage(self) -> None:
		super().display_beverage()

def main() -> None:
	bev = MilkAdder(ChocolateAdder(Expresso()))
	bev.display_beverage()

if __name__ == "__main__":
	main()