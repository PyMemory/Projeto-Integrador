import Fases
import Operacoes
from PontuaçãoFases import Pontuacao

class Fase2:
    def __init__(self):
        self.op = Operacoes.Operacoes()
        self.jm = Fases.JogoMemoria(operacao=self.op.subtracao)
        self.pf = Pontuacao(self.jm)

    def executar_fase(self):        
        self.jm.executar()

    def pontos_fase2(self):
        pf2 = self.pf.pontosFase()
        return pf2
    
# Criar e executar a fase
fase2 = Fase2()
fase2.executar_fase()