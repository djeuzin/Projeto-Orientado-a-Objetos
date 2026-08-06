from abc import ABCMeta, abstractmethod

class Subject(metaclass=ABCMeta):
	observers = None

	def add_observer(self, obs):
		if self.observers == None:
			self.observers = [obs]
		else:
			self.observers.append(obs)

	def remove_observer(self, obs):
		try:
			self.observers.remove(obs)
		except:
			pass

	def notify_observers(self):
		for observer in self.observers:
			observer.update(self)

class Observer(metaclass=ABCMeta):
	@abstractmethod
	def update(self, subject):
		...

class PCD(Subject):
	"""
	Plataforma de coleta de dados
	"""
	temp = 0
	ph = 0
	umidade = 0 
	pa = 0

	def __init__(self, id, location):
		self.id = id
		self.location = location

	def set_temp(self, t):
		self.temp = t
		self.notify_observers()

	def set_ph(self, ph):
		self.ph = ph
		self.notify_observers()

	def set_umidade(self, u):
		self.umidade = u
		self.notify_observers()

	def set_pa(self, p):
		self.pa = p
		self.notify_observers()

class Universidade(Observer):
	def __init__(self, name):
		self.name = name

	def update(self, pcd):
		print(f"{self.name} diz: PCD {pcd.id} no {pcd.location} teve alteração.")

def main():
	UNIFESP = Universidade("UNIFESP")
	UFRGS = Universidade("UFRGS")
	UFRJ = Universidade("UFRJ")

	pcd1 = PCD(1, "Rio Negro")
	pcd2 = PCD(2, "Solimões")
	pcd3 = PCD(3, "Madeira")
	pcd4 = PCD(4, "Tapajós")
	pcd5 = PCD(5, "Xingu")

	pcd1.add_observer(UNIFESP)
	pcd1.add_observer(UFRJ)

	pcd2.add_observer(UNIFESP)
	pcd2.add_observer(UFRGS)

	pcd3.add_observer(UNIFESP)
	pcd3.add_observer(UFRJ)
	pcd3.add_observer(UFRGS)

	pcd4.add_observer(UFRJ)

	pcd5.add_observer(UFRJ)
	pcd5.add_observer(UFRGS)

	pcd1.set_ph(5)

	pcd3.set_umidade(5)

	pcd5.set_pa(5)

	pcd4.set_temp(23)
	print(f"Removendo UNIFESP de {pcd1.location}")
	pcd1.remove_observer(UNIFESP)

	pcd1.set_temp(23)

if __name__ == "__main__":
	main()
