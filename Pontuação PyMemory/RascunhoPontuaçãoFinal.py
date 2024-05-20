import cartas
from PontuaçãoFases import Pontuacao

class PontuacaoFinal:
    def __init__(self):
        self.total_pontos = 0

    def jogar_fase(self):
        # Inicializa uma nova fase do jogo
        game = cartas.JogoMemoria()
        game.executar()
        
        # Calcula a pontuação da fase
        pontuacao = Pontuacao(game)
        pontos = pontuacao.pontosFase()
        
        # Adiciona os pontos da fase ao total
        self.total_pontos += pontos
        print(f"Pontuação da fase: {pontos}")
        print(f"Pontuação total até agora: {self.total_pontos}")

    def jogar(self, num_fases=5):
        for fase in range(num_fases):
            print(f"--- Fase {fase + 1} ---")
            self.jogar_fase()
        print(f"Pontuação final após {num_fases} fases: {self.total_pontos}")

if __name__ == "__main__":
    pontuacao_final = PontuacaoFinal()
    pontuacao_final.jogar()