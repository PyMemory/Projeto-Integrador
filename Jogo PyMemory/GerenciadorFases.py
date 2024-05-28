# GerenciadorFases.py

from Fase0Teste import FaseT
from Fase1 import Fase1
from Fase2 import Fase2
from Fase3 import Fase3
from Fase4 import Fase4
from PontuacaoFinal import PontuacaoFinal

class GerenciadorFases:
    def __init__(self):
        self.fases = [FaseT(), Fase1(), Fase2(), Fase3(), Fase4()]
        self.fase_atual = 0

    def proxima_fase(self):
        if self.fase_atual < len(self.fases) - 1:
            self.fase_atual += 1
            self.fases[self.fase_atual].executar_fase()
        else:
            self.mostrar_pontuacao_final()
            return False  # Indica que não há mais fases disponíveis

    def mostrar_pontuacao_final(self):
        # Implemente aqui a lógica para mostrar a pontuação final
        pontuacao_final = PontuacaoFinal.calculo_pontos()
        return pontuacao_final

# Executar o jogo
