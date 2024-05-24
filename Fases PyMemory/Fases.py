import pygame
import random
from Operacoes import Operacoes

# Definição de cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERDE = (0, 128, 0)
CINZA = (192, 192, 192)

class JogoMemoria:
    def __init__(self, operacao):
        pygame.init()
        self.largura_tela = 1300
        self.altura_tela = 700
        self.espaco_superior = -50  # Ajuste aqui para diminuir mais o espaço acima das cartas
        self.tela = pygame.display.set_mode((self.largura_tela, self.altura_tela), pygame.RESIZABLE)
        pygame.display.set_caption("P Y M E M O R Y")
        self.clock = pygame.time.Clock()

        # Configurações do jogo
        self.NUM_LINHAS = 2
        self.NUM_COLUNAS = 5
        self.MAX_TENTATIVAS = 100

        # Configurações do cartão
        self.largura_cartao = 190
        self.altura_cartao = 220
        self.espacamento = 20

        # Proporção entre a largura da tabela e a largura das cartas
        self.proporcao_tabela_cartao = 1 / 2

        # Configurações do texto
        self.tamanho_fonte = 90
        self.tamanho_fonte_tabela = 40
        self.tamanho_fonte_operacao = 80
        
        # Inicializa as operações matemáticas
        self.operacoes = Operacoes()
        self.operacao_atual = operacao  # Define a operação padrão como adição

        # Inicializa o estado do jogo
        self.numero_escolhido, self.x, self.y, self.resposta, self.operador = self.obter_operacao()  # Obtém a primeira operação
        self.grid = self.criar_grade_cartas()
        self.cartoes = self.criar_cartas()
        self.tentativas = 0
        self.cartao_revelado = []

        # Variáveis de controle de tempo
        self.timer_started = False
        self.timer_end = 0

        # Inicializa a lista de números encontrados
        self.numeros_encontrados = []

    def obter_operacao(self):
        x, y, resposta, operador = self.operacao_atual()
        if y is not None:
            numero_escolhido = resposta
            return numero_escolhido, x, y, resposta, operador
        else:
            return self.obter_operacao()  # Chama novamente até obter uma operação válida


    def criar_grade_cartas(self):
        numeros_cartao = [self.numero_escolhido]
        while len(numeros_cartao) < (self.NUM_LINHAS * self.NUM_COLUNAS // 2):
            numero = random.randint(1, 20)
            if numero != self.numero_escolhido and numero not in numeros_cartao:
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
                y = linha * (self.altura_cartao + self.espacamento) + self.espacamento + self.altura_cartao + self.espaco_superior
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
            # Adiciona o número encontrado à lista
            if carta1['numero'] not in self.numeros_encontrados:
                self.numeros_encontrados.append(carta1['numero'])
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

    def desenhar_tabela_numeros(self):
        # Tamanho e posição da tabela
        largura_tabela = self.largura_cartao * self.proporcao_tabela_cartao
        altura_tabela = self.altura_tela
        x_tabela = self.largura_tela - largura_tabela
        y_tabela = 0
        
        # Desenha o fundo da tabela
        pygame.draw.rect(self.tela, VERDE, (x_tabela, y_tabela, largura_tabela, altura_tabela))
        
        # Configurações do texto
        fonte = pygame.font.Font('SuperMario256.ttf', self.tamanho_fonte_tabela)
        cor_texto = PRETO

        # Desenha os números encontrados na tabela
        for i, numero in enumerate(self.numeros_encontrados):
            texto = fonte.render(str(numero), True, cor_texto)
            x_texto = x_tabela + (largura_tabela - texto.get_width()) / 7 # Centraliza horizontalmente
            y_texto = y_tabela + i * 150 + 15 # Mudar a altura dos numeros
            self.tela.blit(texto, (x_texto, y_texto))

    def desenhar_operacao_matematica(self):
        # Define o retângulo branco para a área da operação matemática
        largura_operacao = 600
        altura_operacao = self.altura_cartao + self.espaco_superior
        x_operacao =  200
        y_operacao = 10
        
        pygame.draw.rect(self.tela, BRANCO, (x_operacao, y_operacao, largura_operacao, altura_operacao))
        
        # Desenha a operação matemática atual na tela
        fonte = pygame.font.Font('SuperMario256.ttf', self.tamanho_fonte_operacao)
        cor_texto = PRETO
        texto_operacao = f"{self.x} {self.operador} {self.y} = ?"
        texto = fonte.render(texto_operacao, True, cor_texto)
        x_texto = self.largura_tela - 1020  # Alinhado à direita
        y_texto = 70
        self.tela.blit(texto, (x_texto, y_texto))

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

            # Desenha a tabela de números encontrados
            self.desenhar_tabela_numeros()
            
            # Desenha a operação matemática
            self.desenhar_operacao_matematica()

            pygame.display.flip()
            self.clock.tick(60)

#Executando o jogo
#jogo = JogoMemoria()
#jogo.executar()