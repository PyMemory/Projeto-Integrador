import Fases
import Operacoes
from PontuaçãoFases import Pontuacao

class Fase3:
    def __init__(self):
        self.op = Operacoes.Operacoes()
        self.jm = Fases.JogoMemoria(operacao=self.op.multiplicacao)
        self.pf = Pontuacao(self.jm)

    def executar_fase(self):        
        self.jm.executar()
        
        tentativas = self.pf.tentativas()
        
    def pontos_fase3(self):
        pf3 = self.pf.pontosFase()
        return pf3
    
# Criar e executar a fase
fase3 = Fase3()
fase3.executar_fase()