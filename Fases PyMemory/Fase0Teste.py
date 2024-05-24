import Fases
import Operacoes
from PontuaçãoFases import Pontuacao

class FaseT:
    def __init__(self):
        self.op = Operacoes.Operacoes()
        self.jm = Fases.JogoMemoria(operacao= Operacoes.operacaoAd)
        self.pf = Pontuacao(self.jm)

    def executar_fase(self):        
        self.jm.executar()
        
    
# Criar e executar a fase
faseT = FaseT()
faseT.executar_fase()