# Rafael Freire Machado Gonçalves
# RA: 163977

class Pessoa:
	"""
	Classe pessoa

	Atributos:
	nome (str): Nome da pessoa
	cpf (str): Identificador único
	"""
	nome: str
	cpf: str

	def __init__(self, nome: str, cpf: str):
		self.nome = nome
		self.cpf = cpf

class Empresa:
	"""
	Classe empresa

	Atributos:
	responsavel (Pessoa): Pessoa responsável
	"""
	responsavel: Pessoa

	def __init__(self, pessoa: Pessoa):
		self.responsavel = pessoa

class SingletonMeta(type):
	"""
	Classe abstrata singleton
	Utilizada pra implementar o padrão
	"""
	_instances = {}

	def __call__(cls, *args, **kwargs):
		if cls not in cls._instances:
			instance = super().__call__(*args, **kwargs)
			instance.pessoas = {}
			instance.empresas = {}
			cls._instances[cls] = instance
		return cls._instances[cls]

class Builder(metaclass=SingletonMeta):
	"""
	Classe builder

	Atributos:
	pessoas (dict[str, Pessoa]): Tabela que armazena pessoas criadas
	empresas (dict[str, Empres]): Tabela que armazena empresas criadas

	Métodos:
	get_pessoa(str, str) -> Pessoa: Retorna uma pessoa da tabela
	get_empresa(str, str) -> Empresa: Retoran uma empresa da tabela
	"""
	pessoas: dict[str, Pessoa]
	empresas: dict[str, Empresa]

	def get_pessoa(self, nome: str, cpf: str) -> Pessoa:
		if self.pessoas.get(cpf) is None:
			self.pessoas[cpf] = Pessoa(nome, cpf)
		else:
			print(f"Pessoa com o mesmo CPF já cadastrada.")
		return self.pessoas[cpf]

	def get_empresa(self, nome: str, cpf: str) -> Empresa:
		pessoa = self.get_pessoa(nome, cpf)
		if self.empresas.get(pessoa.cpf) is None:
			self.empresas[pessoa.cpf] = Empresa(pessoa)
		return self.empresas[pessoa.cpf]


def main():
	nomes = ["Rafael", "Sophia", "Damon", "Tim", "Milton"]
	cpfs = ["123454", "21251", "1345135", "1325125", "12351235"]

	builder = Builder()

	empresas = []
	for nome, cpf in zip(nomes, cpfs):
		empresas.append(builder.get_empresa(nome, cpf))

	for empresa in empresas:
		print(f"Responsável: {empresa.responsavel.nome}. CPF: {empresa.responsavel.cpf}")

	# Empresa já existente:
	empresa = builder.get_empresa("Djeu", cpfs[1])
	print(f"Emrpesa de: {empresa.responsavel.nome}")

	pessoa = builder.get_pessoa("Intruso", cpfs[2])
	
	for p in builder.pessoas:
		print(f"{builder.pessoas[p].nome}-{builder.pessoas[p].cpf}")

if __name__ == "__main__":
	main()