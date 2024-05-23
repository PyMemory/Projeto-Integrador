import pygame
import random

# Definição de cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERDE = (0, 128, 0)
CINZA = (192, 192, 192)

class JogoMemoria:
    def __init__(self):
        pygame.init()
        self.largura_tela = 1200
        self.altura_tela = 671
        self.tela = pygame.display.set_mode((self.largura_tela, self.altura_tela), pygame.RESIZABLE)
        pygame.display.set_caption("P Y M E M O R Y")
        self.clock = pygame.time.Clock()

        # Configurações do jogo
        self.NUM_LINHAS = 2
        self.NUM_COLUNAS = 5
        self.MAX_TENTATIVAS = 100

        # Configurações do cartão
        self.largura_cartao = 216
        self.altura_cartao = 310
        self.espacamento = 20

        # Configurações do texto
        self.tamanho_fonte = 90

        # Inicializa o estado do jogo
        self.numero_escolhido = 20 # Número escolhido pelo jogador
        self.grid = self.criar_grade_cartas()
        self.cartoes = self.criar_cartas()
        self.tentativas = 0
        self.cartao_revelado = []

        # Variáveis de controle de tempo
        self.timer_started = False
        self.timer_end = 0

    def criar_grade_cartas(self):
        numeros_cartao = [self.numero_escolhido]
        for _ in range((self.NUM_LINHAS * self.NUM_COLUNAS // 2) - 1):
            numero = random.randint(1, 100)
            while numero == self.numero_escolhido:
                numero = random.randint(1, 100)
            numeros_cartao.append(numero)
        numeros_cartao *= 2  # Duplica os números para formar os pares
        random.shuffle(numeros_cartao)
        grade = []
        for _ in range(self.NUM_LINHAS):
            linha = []
            for _ in range(self.NUM_COLUNAS):
                numero = numeros_cartao.pop()
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

    def trocar_cartoes(self, numero):
        if len(self.cartao_revelado) == 2:
            for carta in self.cartao_revelado:
                carta['numero'] = numero
            self.cartao_revelado.clear()

    def executar(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    self.cartao_clicado(x, y)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and len(self.cartao_revelado) == 2:
                        numero_trocado = int(input("Digite o número para trocar as cartas: "))
                        self.trocar_cartoes(numero_trocado)
                    elif event.key == pygame.K_n:
                        novo_numero = int(input("Digite o novo número: "))
                        self.numero_escolhido = novo_numero
                        self.grid = self.criar_grade_cartas()
                        self.cartoes = self.criar_cartas()

            if self.timer_started and pygame.time.get_ticks() >= self.timer_end:
                self.timer_started = False
                for carta in self.cartao_revelado:
                    carta['revelado'] = False
                self.cartao_revelado.clear()

            self.tela.fill(VERDE)
            for carta in self.cartoes:
                cor = BRANCO if carta['revelado'] else CINZA
                pygame.draw.rect(self.tela, cor, carta['rect'])
                if carta['revelado']:
                    fonte = pygame.font.Font('SuperMario256.ttf', self.tamanho_fonte)
                    texto = fonte.render(str(carta['numero']), True, VERDE)
                    texto_rect = texto.get_rect(center=carta['rect'].center)
                    self.tela.blit(texto, texto_rect)

            pygame.display.flip()
            self.clock.tick(60)

# Executando o jogo
jogo = JogoMemoria()
jogo.executar()