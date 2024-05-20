import cartas

class Pontuacao:
    def __init__(self, jogo):
        self.jogo = jogo

    def tentativas(self):
        return self.jogo.get_tentativas() - 1

    def pontosFase(self):
        tentativa = self.tentativas()
        if tentativa <= 4:
            pontos = 10
        elif tentativa <= 8:
            pontos = 8
        elif tentativa <= 12:
            pontos = 5
        else:
            pontos = 3
        return pontos

