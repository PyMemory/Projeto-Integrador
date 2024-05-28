from GerenciadorFases import GerenciadorFases
from Fases import JogoMemoria
import pygame

if __name__ == "__main__":
    gerenciador = GerenciadorFases()
    while True:
        jogo = JogoMemoria(operacao=None, gerenciador_fases=gerenciador)
        jogo.executar() 
        if not gerenciador.proxima_fase():
            print("Não há mais fases disponíveis.")
            pygame.quit()  # Sai do loop se não houver mais fases disponíveis
