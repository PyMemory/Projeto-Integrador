#Fase0Teste.py
import Fases
import Operacoes
from PontuaçãoFases import Pontuacao

class FaseT:
    def __init__(self):
        self.op = Operacoes.Operacoes()
        self.jm = Fases.JogoMemoria(operacao=self.op.adicao)  # Corrigido para usar uma operação válida
        self.pf = Pontuacao(self.jm)

    def executar_fase(self):        
        self.jm.executar()
    
    def pontos_fase0(self):
        pf0 = self.pf.pontosFase()
        return pf0
    
#faseT = Fase0Teste.FaseT()
#faseT.executar_fase()
