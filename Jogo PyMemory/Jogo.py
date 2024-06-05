# Jogo.py
import pygame
import Fase0Teste
import Fase1
import Fase2
import Fase3
import Fase4
import os

class Jogo:
    @staticmethod
    def calcular_pontuacao_final(pontos_fase1, pontos_fase2, pontos_fase3, pontos_fase4):
        pontuacao_final = pontos_fase1 + pontos_fase2 + pontos_fase3 + pontos_fase4
        if 30 <= pontuacao_final <= 40:
            classificacao = "Incrivel"
        elif 20 <= pontuacao_final <= 29:
            classificacao = "Otima"
        else:
            classificacao = "Boa"
        return pontuacao_final, classificacao
    
    @staticmethod
    def mostrar_tela_final(pontuacao_final, classificacao):
        pygame.init()
        largura_tela = 1300
        altura_tela = 700
        tela = pygame.display.set_mode((largura_tela, altura_tela))
        pygame.display.set_caption("Tela Final")
        imagem = pygame.image.load(os.path.join("assets", "florestafinal.png"))
        
        fonte = pygame.font.Font('RetroMario-Regular.otf', 50) 
        texto1 = fonte.render("Parabéns, você completou o jogo PyMemory,", True, (0, 0, 0))
        texto2 = fonte.render(f"Pontuação: {pontuacao_final}", True, (0, 0, 0))
        texto3 = fonte.render(f"Classificação: {classificacao}", True, (0, 0, 0))
        texto4 = fonte.render(f"este foi o seu desempenho:", True, (0, 0, 0))
        
        tela.blit(imagem, (0, 0))

        tela.blit(texto1, (150, 180))
        tela.blit(texto4, (380, 230))
        tela.blit(texto2, (470, 300))
        tela.blit(texto3, (400, 350))

        pygame.display.flip()

        esperando = True
        while esperando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    esperando = False

        pygame.quit()

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

        # Mostrar tela final
        Jogo.mostrar_tela_final(pontuacao_final, classificacao)