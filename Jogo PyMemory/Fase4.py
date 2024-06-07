#Fase4.py
import Fases
import Operacoes
from PontuaçãoFases import Pontuacao

class Fase4:
    def __init__(self):
        self.op = Operacoes.Operacoes()
        self.jm = Fases.JogoMemoria(operacao=self.op.divisao, ultima_fase=True)
        self.pf = Pontuacao(self.jm)

    def executar_fase(self):        
        self.jm.executar()
        
    def pontos_fase4(self):
        pf4 = self.pf.pontosFase()
        return pf4
    
# Criar e executar a fase
#fase4 = Fase4.Fase4()
#fase4.executar_fase()
