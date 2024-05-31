# Jogo.py

import Fase0Teste
import Fase1
import Fase2
import Fase3
import Fase4

class Jogo:
    @staticmethod
    def calcular_pontuacao_final(pontos_fase1, pontos_fase2, pontos_fase3, pontos_fase4):
        pontuacao_final = pontos_fase1 + pontos_fase2 + pontos_fase3 + pontos_fase4
        if 30 <= pontuacao_final <= 40:
            classificacao = "Incrível"
        elif 20 <= pontuacao_final <= 29:
            classificacao = "Ótima"
        else:
            classificacao = "Boa"
        return pontuacao_final, classificacao

    @staticmethod
    def jogo():
        # Executando fase 0
        fase0 = Fase0Teste.FaseT()
        fase0.executar_fase()

        # Executando fase 1
        fase1 = Fase1.Fase1()
        fase1.executar_fase()
        pontos_fase1 = fase1.pontos_fase1()

        # Executando fase 2
        fase2 = Fase2.Fase2()
        fase2.executar_fase()
        pontos_fase2 = fase2.pontos_fase2()

        # Executando fase 3
        fase3 = Fase3.Fase3()
        fase3.executar_fase()
        pontos_fase3 = fase3.pontos_fase3()

        # Executando fase 4
        fase4 = Fase4.Fase4()
        fase4.executar_fase()
        pontos_fase4 = fase4.pontos_fase4()

        # Calcular pontuação final
        pontuacao_final, classificacao = Jogo.calcular_pontuacao_final(pontos_fase1, pontos_fase2, pontos_fase3, pontos_fase4)
