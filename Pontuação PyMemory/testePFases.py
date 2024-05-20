from PontuaçãoFases import Pontuacao
import cartas

if __name__ == "__main__":
    jogo = cartas.JogoMemoria()
    jogo.executar()


ponts = Pontuacao(jogo)
print("Tentativas: ", ponts.tentativas())
print("Pontos:", ponts.pontosFase())