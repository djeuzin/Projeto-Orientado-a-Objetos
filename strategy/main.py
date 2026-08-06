from abc import ABC, abstractmethod
from datetime import datetime 

class EstrategiaDia(ABC):
    @property
    @abstractmethod
    def prioridade(self) -> str:
        pass
    @abstractmethod
    def executar(self, usuario: str, informacao: str, dia_semana: str) -> str:
        pass


class EstrategiaSegundaFeira(EstrategiaDia):
    @property
    def prioridade(self) -> str:
        return "ALTA"  
        
    def executar(self, usuario: str, informacao: str, dia_semana: str) -> str:
        return f"organize suas prioridades. A meta e '{informacao}'."
        
        
class EstrategiaTercaFeira(EstrategiaDia):
    @property  
    def prioridade(self) -> str:
        return "ALTA"
        
    def executar(self, usuario: str, informacao: str, dia_semana: str) -> str:
        return f"avance nas tarefas pendentes. A meta e '{informacao}'."
        
class EstrategiaQuartaFeira(EstrategiaDia):
    @property
    def prioridade(self) -> str:
        return "MÉDIA"
        
    def executar(self, usuario: str, informacao: str, dia_semana: str) -> str:
        return f"dia de revisão, verifique o andamento da atividade '{informacao}'."
        
class EstrategiaQuintaFeira(EstrategiaDia):
    @property
    def prioridade(self) -> str:
        return "BAIXA"
        
    def executar(self, usuario: str, informacao: str, dia_semana: str) -> str:
        return f"colabore com alguem da equipe. inicie com '{informacao}'."

class EstrategiaSextaFeira(EstrategiaDia):
    @property
    def prioridade(self) -> str:
        return "ALTA"

    def executar(self, usuario: str, informacao: str, dia_semana: str) -> str:
        return f"dia de descansar, né? pode ir para a farra e {informacao}"

class EstrategiaSabado(EstrategiaDia):
    @property
    def prioridade(self) -> str:
        return "MÉDIA"

    def executar(self, usuario: str, informacao: str, dia_semana: str) -> str:
        return f"dia de recuperar as energias com {informacao}"

class EstrategiaDomingo(EstrategiaDia):
    @property
    def prioridade(self) -> str:
        return "BAIXA"

    def executar(self, usuario: str, informacao: str, dia_semana: str) -> str:
        return f"dia de se preparar para a semana. Comece com {informacao}"

class EstrategiaInvalida(EstrategiaDia):
    @property
    def prioridade(self) -> str:
        return "INVÁLIDA"
        
    def executar(self, usuario: str, informacao: str, dia_semana: str) -> str:
        return f"Estratégia para {dia_semana} inexistente."
    
    
class GerenciadorRotina:
    def __init__(self):
        self._estrategias = {
            "segunda-feira": EstrategiaSegundaFeira(),
            "terça-feira": EstrategiaTercaFeira(),
            "quarta-feira": EstrategiaQuartaFeira(),
            "quinta-feira": EstrategiaQuintaFeira()
        }
        
        self._dias_pro_extenso = {
            0: "segunda-feira", 1: "terça-feira", 2: "quarta-feira",
            3: "quinta-feira", 4: "sexta-feira", 5: "sabado", 6: "domingo"
        }

    def obter_dia_atual_extenso(self) -> str:
        """Requisito 1"""
        indice_dia = datetime.now().weekday()
        return self._dias_pro_extenso[indice_dia]
    
    def executar_rotina(self, usuario: str, dia_semana: str, informacao: str) -> str:
        dia_formatado = dia_semana.lower().strip()

        estrategia = self._estrategias.get(dia_formatado, EstrategiaInvalida())
        mensagem = estrategia.executar(usuario, informacao, dia_formatado)
        
        return (f"usuario: {usuario}\n"
                f"dia consultado: {dia_formatado}\n"
                f"prioridade: {estrategia.prioridade}\n" 
                f"mensagem: {mensagem}\n"
                f"{'-'*10}")


if __name__ == "__main__":
    gerenciador = GerenciadorRotina()

    saida_manual = gerenciador.executar_rotina(
        usuario="Nick", 
        dia_semana="quarta-feira", 
        informacao="definir cronograma do projeto e dividir as funcoes do trabalho"
    )
    
    print(saida_manual)


    print("\nconsulta automatica baseada no dia de hoje (Requisito 1)")
    dia_hoje = gerenciador.obter_dia_atual_extenso()
    saida_automatica = gerenciador.executar_rotina(
        usuario="Nick", 
        dia_semana=dia_hoje, 
        informacao="Revisar código do padrão Strategy"
    )
    print(saida_automatica)
    
    saida_manual2 = gerenciador.executar_rotina(
        usuario="Rafael",
        dia_semana="dia-que-nao-existe",
        informacao="Fazer pull request na atividade"
    )

    print(saida_manual2)