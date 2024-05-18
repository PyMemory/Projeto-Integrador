import pygame
import random
import subprocess

# Definição de cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERDE = (0, 128, 0)
CINZA = (192, 192, 192)

class JogoMemoria:
    
    
    def __init__(self):
        pygame.init()
        self.largura_tela = 800
        self.altura_tela = 600
        self.tela = pygame.display.set_mode((self.largura_tela, self.altura_tela))
        pygame.display.set_caption("Jogo da Memória")
        self.clock = pygame.time.Clock()

        # Configurações do jogo
        self.NUM_LINHAS = 2
        self.NUM_COLUNAS = 5
        self.NUMEROS_CARTAO = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        self.MAX_TENTATIVAS = 100

        # Configurações do cartão
        self.largura_cartao = 100
        self.altura_cartao = 100
        self.espacamento = 10

        # Inicializa o estado do jogo
        self.grid = self.criar_grade_cartas()
        self.cartoes = self.criar_cartas()
        self.tentativas = 0
        self.cartao_revelado = []

        # Variáveis de controle de tempo
        self.timer_started = False
        self.timer_end = 0

    def criar_grade_cartas(self):
        num = (self.NUMEROS_CARTAO * 2)[:self.NUM_LINHAS * self.NUM_COLUNAS // 2]
        num = num * 2
        random.shuffle(num)
        grade = []
        for _ in range(self.NUM_LINHAS):
            linha = []
            for _ in range(self.NUM_COLUNAS):
                numero = num.pop()
                linha.append(numero)
            grade.append(linha)
        return grade

    def criar_cartas(self):
        cartoes = []
        for linha in range(self.NUM_LINHAS):
            for coluna in range(self.NUM_COLUNAS):
                numero = self.grid[linha][coluna]
                x = coluna * (self.largura_cartao + self.espacamento) + self.espacamento
                y = linha * (self.altura_cartao + self.espacamento) + self.espacamento
                cartoes.append({'numero': numero, 'rect': pygame.Rect(x, y, self.largura_cartao, self.altura_cartao), 'revelado': False})
        return cartoes

    def cartao_clicado(self, x, y):
        for carta in self.cartoes:
            if carta['rect'].collidepoint(x, y) and not carta['revelado'] and len(self.cartao_revelado) < 2:
                carta['revelado'] = True
                self.cartao_revelado.append(carta)
                if len(self.cartao_revelado) == 2:
                    self.verificar_correspondencia()
        

    def verificar_correspondencia(self):
        self.get_tentativas()
        carta1, carta2 = self.cartao_revelado
        if carta1['numero'] == carta2['numero']:
            self.cartao_revelado.clear()
            if self.verificar_vitoria():
                self.exibir_mensagem_vitoria()
        else:
            self.timer_started = True
            self.timer_end = pygame.time.get_ticks() + 1000  # Mantém os números visíveis por 1 segundo
        

    def verificar_vitoria(self):
        for carta in self.cartoes:
            if not carta['revelado']:
                return False
        return True

    def exibir_mensagem_vitoria(self):
        pygame.display.set_caption("Parabéns! Você venceu!")

    def atualizar_pontuacao(self):
        self.tentativas += 1
        if self.tentativas >= self.MAX_TENTATIVAS:
            pygame.display.set_caption("Fim de jogo. Você atingiu o limite de tentativas.")
        
    
    def get_tentativas(self):
        self.tentativas += 1
        return self.tentativas
    
    def executar(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    self.cartao_clicado(x, y)

            if self.timer_started and pygame.time.get_ticks() >= self.timer_end:
                self.timer_started = False
                for carta in self.cartao_revelado:
                    carta['revelado'] = False
                self.cartao_revelado.clear()

            self.tela.fill(BRANCO)
            for carta in self.cartoes:
                cor = VERDE if carta['revelado'] else CINZA
                pygame.draw.rect(self.tela, cor, carta['rect'])
                if carta['revelado']:
                    fonte = pygame.font.Font(None, 36)
                    texto = fonte.render(carta['numero'], True, PRETO)
                    texto_rect = texto.get_rect(center=carta['rect'].center)
                    self.tela.blit(texto, texto_rect)

            pygame.display.flip()
            self.clock.tick(60)
    
if __name__ == "__main__":
    jogo = JogoMemoria()
    jogo.executar()
    

    
    
