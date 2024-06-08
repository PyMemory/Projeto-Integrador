#Fases.py
import pygame
import random
import os
from Operacoes import Operacoes

# Definição de cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERDE = (0, 128, 0)
CINZA = (192, 192, 192)
VERMELHO = (255, 0, 0)


imagem = pygame.image.load(os.path.join("assets","florestafases.png"))

class JogoMemoria:

    def __init__(self, operacao, gerenciador_fases=None, ultima_fase = False):
        pygame.init()
        self.largura_tela = 1300
        self.altura_tela = 700
        self.espaco_superior = -50  # Ajuste aqui para diminuir mais o espaço acima das cartas
        self.tela = pygame.display.set_mode((self.largura_tela, self.altura_tela))
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

        # Inicializa os botões
        self.botoes = self.criar_botoes()
        self.vitoria = False

        # Gerenciador de fases
        self.gerenciador_fases = gerenciador_fases
        self.ultima_fase = ultima_fase

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
                self.vitoria = True  # Marca a vitória
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
        pygame.display.set_caption("Parabéns, você encontrou todos os pares!")

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

    def desenhar_operacao_matematica(self):
        # Define o retângulo branco para a área da operação matemática
        largura_operacao = 600
        altura_operacao = 100
        x_operacao =  200
        y_operacao = 50
        
        pygame.draw.rect(self.tela, CINZA, (x_operacao, y_operacao, largura_operacao, altura_operacao))
        
        # Desenha a operação matemática atual na tela
        fonte = pygame.font.Font('RetroMario-Regular.otf', self.tamanho_fonte_operacao)
        cor_texto = PRETO
        texto_operacao = f"{self.x} {self.operador} {self.y} = ?"
        texto = fonte.render(texto_operacao, True, cor_texto)
        x_texto = self.largura_tela - 1020  # Alinhado à direita
        y_texto = 70
        self.tela.blit(texto, (x_texto, y_texto))

    def criar_botoes(self):
        largura_botao = 200
        altura_botao = 100
        espacamento = 20
        x_base = self.largura_tela - largura_botao - espacamento
        y_base = 100
        botoes = []
        for i in range(5):
            y = y_base + i * (altura_botao + espacamento)
            botao = pygame.Rect(x_base, y, largura_botao, altura_botao, border_radius=20)
            botoes.append({'rect': botao, 'numero': None, 'ativo': False, 'clicado': False})
        return botoes

    def desenhar_botoes(self):
        if self.vitoria:
            fonte = pygame.font.Font('RetroMario-Regular.otf', self.tamanho_fonte_tabela)
            for botao in self.botoes:
                cor_botao = VERMELHO if botao['clicado'] else BRANCO
                pygame.draw.rect(self.tela, cor_botao, botao['rect'], border_radius=20)
                if botao['ativo']:
                    texto = fonte.render(str(botao['numero']), True, PRETO)
                    texto_rect = texto.get_rect(center=botao['rect'].center)
                    self.tela.blit(texto, texto_rect)

    def configurar_botoes(self):
        numeros_unicos = list(set(self.numeros_encontrados))
        for i, botao in enumerate(self.botoes):
            if i < len(numeros_unicos):
                botao['numero'] = numeros_unicos[i]
                botao['ativo'] = True

    def mostrar_popup(self, texto1, texto2, texto3):
        popup_largura = 490
        popup_altura = 300
        x_popup = (self.largura_tela - popup_largura) // 2
        y_popup = (self.altura_tela - popup_altura) // 2
        
        fonte = pygame.font.Font('RetroMario-Regular.otf', 40)
        texto1_render = fonte.render(texto1, True, BRANCO)
        texto2_render = fonte.render(texto2, True, BRANCO)
        texto3_render = fonte.render(texto3, True, BRANCO)
        
        popup_rect = pygame.Rect(x_popup, y_popup, popup_largura, popup_altura)
        pygame.draw.rect(self.tela, VERDE, popup_rect, border_radius=20)
        self.tela.blit(texto1_render, (x_popup + 25, y_popup + 50))
        self.tela.blit(texto2_render, (x_popup + 40, y_popup + 200))
        self.tela.blit(texto3_render, (x_popup + 25, y_popup + 250))
        
        pygame.display.flip()
        pygame.time.delay(5000)

    def checar_botoes(self, x, y):
        for botao in self.botoes:
            if botao['rect'].collidepoint(x, y) and botao['ativo']:
                if botao['numero'] == self.resposta:
                    if self.ultima_fase:
                        self.mostrar_popup("Parabéns, você acertou!", "  ", "  ")
                    else:
                        self.mostrar_popup("Parabéns, você acertou!", "       A próxima fase    ", "  começa em 5 segundos!")
                    pygame.display.quit() 
                    return
                else:
                    botao['clicado'] = True

    def executar(self):
        while True:
            try:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.display.quit()
                        return
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        x, y = pygame.mouse.get_pos()
                        self.cartao_clicado(x, y)
                        self.checar_botoes(x, y)
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

                
                self.tela.blit(imagem, (0, 0))
                for carta in self.cartoes:
                    cor = BRANCO if carta['revelado'] else CINZA
                    pygame.draw.rect(self.tela, cor, carta['rect'])
                    if carta['revelado']:
                        fonte = pygame.font.Font('RetroMario-Regular.otf', self.tamanho_fonte)
                        texto = fonte.render(str(carta['numero']), True, VERDE)
                        texto_rect = texto.get_rect(center=carta['rect'].center)
                        self.tela.blit(texto, texto_rect)

                
                
                # Desenha a operação matemática
                self.desenhar_operacao_matematica()

                # Desenha os botões se a vitória foi alcançada
                self.desenhar_botoes()

                pygame.display.flip()
                self.clock.tick(60)

                # Configura os botões após a vitória
                if self.vitoria:
                    self.configurar_botoes()
            except pygame.error:
                return
