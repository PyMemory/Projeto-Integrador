# Jogo.py
from Fase0Teste import FaseT
from Fase1 import Fase1
from Fase2 import Fase2
from Fase3 import Fase3
from Fase4 import Fase4

class Jogo:
    def __init__(self):
        self.fases = [
            FaseT(),
            Fase1(),
            Fase2(),
            Fase3(),
            Fase4()
        ]

    def Pontuacao_Final(self):
        pontuacaoF = 0
        pontuacaoF = sum(Fase1.pontos_fase1(), Fase2.pontos_fase2(),
                         Fase3.pontos_fase3(), Fase4.pontos_fase4())
        texto = str
        if pontuacaoF > 40:
            texto = "Incrível!"
        elif pontuacaoF > 25:
            texto = "Ótimo!"
        elif pontuacaoF > 15:
            texto = "Boa!"
            
        return pontuacaoF, texto


