from abc import ABCMeta, abstractmethod

# Constantes para indicar mudanças
URA = 1
PA = 2
TEMP = 3
PH = 0

class Subject(metaclass=ABCMeta):
	"""
	Clase que indica o sujeito que será observado.

	@atributes
	- observers: list[Observer]. Lista de observadores que 
	devem ser notificados.

	@methods
	- add_observer(item: Observer). Adiciona um observer a lista
	de observadores.
	- remove_observer(item: Observer). Remove um observer.
	- notify_observer(change: int). Notifica os observadores
	chamando o callback "update" do observador passando a 
	mudança como argumento.
	"""
	observers = None

	def add_observer(self, obs):
		if self.observers == None:
			self.observers = [obs]
		else:
			self.observers.append(obs)

	def remove_observer(self, obs):
		try:
			obs.changes.pop(self.id)
			self.observers.remove(obs)
		except:
			pass

	def notify_observers(self, change: int):
		for observer in self.observers:
			observer.update(self, change)

class Observer(metaclass=ABCMeta):
	"""
	Classe abstrata do observador do sujeito.

	@methods
	- update(subject: Subject, change: int). Callback padrão
	que deve ser chamado para notificar o observador.
	"""
	@abstractmethod
	def update(self, subject, change):
		...

class PCD(Subject):
	"""
	Classe que implementa a plataforma de controle.

	@attributes
	- temp: int. Temperatura.
	- ph: int. PH.
	- umidade: int. Umidade.
	- pa: int. Pressão atmosférica.
	- id: int. Identificador do PCD.
	- location: str. Nome do rio onde está instalado.

	@methods
	- PCD(id: int, location: str). Inicializa id e location.
	- set_temp(t: int). Configura a temperatura para t e 
	notifica os observadores.
	- set_ph(ph: int). ...
	- set_umidade(u: int). ...
	- set_pa(p: int). ...
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
		self.notify_observers(TEMP)

	def set_ph(self, ph):
		self.ph = ph
		self.notify_observers(PH)

	def set_umidade(self, u):
		self.umidade = u
		self.notify_observers(URA)

	def set_pa(self, p):
		self.pa = p
		self.notify_observers(PA)

class Universidade(Observer):
	"""
	Classe que represetna uma universidade que observa
	PCDs.

	@attributes
	- name: str. Nome da universidade.
	- changes: dict{int: list[int]}. Dicionário que armazena as mudanças
	observadas para cada PCD observado.

	@methods
	- Universidade(name: str). Inicializa o nome da univseridade
	e a lista de mudanças.
	- update(pcd: int, change: int). Callback que é chamado
	pelo sujeito observado pela univsersidade. Altera o vetor
	de mudanças na posição correspondente. Se todas as variáveis
	sofreram mudança, exibe na tela para o usuário.
	"""
	def __init__(self, name):
		self.name = name
		self.changes = {}

	def update(self, pcd, change):
		if self.changes.get(pcd.id) == None:
			self.changes[pcd.id] = [0 for i in range(4)]
		self.changes[pcd.id][change] = 1

		if sum(self.changes[pcd.id]) == 4:
			self.changes[pcd.id] = [0 for i in range(4)]
			print(f"{self.name} diz: Rio {pcd.location} sofreu mudanças em todas as variáveis.")

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
	pcd1.set_temp(9)
	pcd1.set_pa(1)
	pcd1.set_umidade(3)


	pcd4.set_temp(23)
	print(f"Removendo UNIFESP de {pcd1.location}")
	pcd1.remove_observer(UNIFESP)

	pcd1.set_temp(23)

if __name__ == "__main__":
	main()
