import Fases
import Operacoes
from PontuaçãoFases import Pontuacao

class Fase1:
    def __init__(self):
        self.op = Operacoes.Operacoes()
        self.jm = Fases.JogoMemoria(operacao=self.op.adicao)
        self.pf = Pontuacao(self.jm)

    def executar_fase(self):        
        self.jm.executar()
        
        tentativas = self.pf.tentativas()
        
    def pontos_fase1(self):
        pf1 = self.pf.pontosFase()
        return pf1
    
# Criar e executar a fase
fase1 = Fase1()
fase1.executar_fase()