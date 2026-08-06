from random import randint

def get_name_texture(species: str) -> int:
	"""
	Mock da represetnação das texturas.
	Na aplicação real, para cada espécie
	haveria um arquivo de textura.
	"""
	match species:
		case "Castanheira-do-pará":
			return 10
		case "Seringueira":
			return 20
		case "Sumaúma":
			return 30
		case "Açaizeiro":
			return 40
		case "Mogno":
			return 50
		case "Andiroba":
			return 60
		case "Copaíba":
			return 70
		case "Pau-brasil":
			return 80
		case "Jatobá":
			return 90
		case "Cedro":
			return 100
		case "Virola":
			return 110
		case "Tauari":
			return 120
		case "Angelim-vermelho":
			return 130
		case "Buriti":
			return 140
		case "Guaraná":
			return 150
		case "Ipê-amarelo-da-amazônia":
			return 160

def get_species_from_id(id: int) -> str:
	match id:
		case 1:
			return "Castanheira-do-pará"
		case 2:
			return "Seringueira"
		case 3:
			return "Sumaúma"
		case 4:
			return "Açaizeiro"
		case 5:
			return "Mogno"
		case 6:
			return "Andiroba"
		case 7:
			return "Copaíba"
		case 8:
			return "Pau-brasil"
		case 9:
			return "Jatobá"
		case 10:
			return "Cedro"
		case 11:
			return "Virola"
		case 12:
			return "Tauari"
		case 13:
			return "Angelim-vermelho"
		case 14:
			return "Buriti"
		case 15:
			return "Guaraná"
		case 16:
			return "Ipê-amarelo-da-amazônia"

class Tree:
	"""
	Classe árvore.

	Atributos imutáveis:
	species (string): nome da espécie
	texture (int): representa a textura da árvore na aplicação gráfica

	Atributos mutáveis:
	height (int): altura da árvore
	radius (int): raio do tronco
	leaf_density (int): densidade das folhas

	Tamanho em memória da classe = 1728 bits ou 216 bytes
	Assumindo inteiros de 64 bits.

	Considerando um arquivo de textura de 1mb,
	a classe ocupa certa de 1.2mb de memória.
	"""
	species: str
	texture: int

	height: int
	radius: int
	leaf_density: int

	def __init__(self, species: str, texture: int):
		self.species = species
		self.texture = texture

	def set_height(self, h: int) -> None:
		self.height = h

	def set_radius(self, r: int) -> None:
		self.radius = r

	def set_leaf_dentisty(self, ld: int) -> None:
		self.leaf_density = ld

	def draw(self, pos: (int, int)) -> None:
		pass
		#print(f"""Species: {self.species}; 
		#	Height: {self.height}; 
		#	Radius: {self.radius}; 
		#	Leaf density: {self.leaf_density};
		#	Position: {pos}""")

class TreeFactory:
	instances: dict[str, Tree]

	def __init__(self):
		self.instances = {}

	def get_instance(self, species: str) -> Tree:
		if species in self.instances.keys():
			return self.instances[species]

		texture = get_name_texture(species)
		self.instances[species] = Tree(species, texture)
		return self.instances[species]

def main():
	"""
	Para trabalhar com 30,000 árvores foram necessários apenas 
	16 instâncias, cerca de 7.2mb de memória.
	Se para cada árvore necessária fosse obrigatória a instanciação
	de um objeto, a quantidade de memória utilizada seria de cerca de
	216,000mb, ou 216Gb de memória.
	"""
	flyTree = TreeFactory()

	for i in range(30000):
		tree = flyTree.get_instance(get_species_from_id(randint(1, 16)))
		tree.set_height(randint(10, 20))
		tree.set_radius(randint(5, 30))
		tree.set_leaf_dentisty(randint(7, 100))
		tree.draw((randint(1, 300), randint(1, 300)))

	print(f"Quantidade de objetos instanciados: {len(flyTree.instances.keys())}")

if __name__ == "__main__":
	main()
