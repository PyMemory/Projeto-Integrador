import tkinter as tk
from tkinter import messagebox
import random

class JogoMemoria:
    def __init__(self, master):
        
        #Inicializa o jogo de memória.

        #Args:
            #master: A janela principal (root) do Tkinter.
        
        self.master = master
        self.master.title('pymemory')
        self.master.configure(bg="#343a40")

        # Configurações do jogo
        self.NUM_LINHAS = 2
        self.NUM_COLUNAS = 10
        self.NUMEROS_CARTAO = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        self.MAX_TENTATIVAS = 100
        self.tamanho_numero = 30

        # Representantes das cartas
        self.grid = self.criar_grade_cartas()
        self.criar_cartas()
        self.label_tentativas = tk.Label(master, text=f"Tentativas: 0/{self.MAX_TENTATIVAS}", fg="#ffffff", bg="#343a40", font=('Arial', 12, 'bold'))
        self.label_tentativas.grid(row=self.NUM_LINHAS+1, columnspan=self.NUM_COLUNAS, padx=10, pady=10)

        # Rastreando o estado do jogo
        self.tentativas = 0
        self.cartao_revelado = []

    def criar_grade_cartas(self):
        
        #Cria a grade de cartas embaralhadas.

        #Returns:
            #grid: Uma lista 2D representando a grade de cartas.
        
        num = (self.NUMEROS_CARTAO * 2)[:self.NUM_LINHAS * self.NUM_COLUNAS // 2]  # Ajuste para garantir que haja cartões suficientes
        num = num * 2  # Duplica os números para garantir que haja um par de cada
        random.shuffle(num)
        grid = []

        for _ in range(self.NUM_LINHAS):
            linha = []
            for _ in range(self.NUM_COLUNAS):
                numero = num.pop()
                linha.append(numero)
            grid.append(linha)
        return grid

    def criar_cartas(self):
        
        #Cria os botões representando as cartas na interface gráfica.
        
        self.cartoes = []
        for linha in range(self.NUM_LINHAS):
            linha_de_cartoes = []
            for col in range(self.NUM_COLUNAS):
                numero = self.grid[linha][col]
                cartao = tk.Button(self.master, width=8, height=4, text=" ", bg='green', fg='black', relief=tk.RAISED, bd=3,
                                   font=('Arial', self.tamanho_numero, 'bold'),
                                   command=lambda l=linha, c=col: self.cartao_clicado(l, c))
                cartao.grid(row=linha, column=col, padx=5, pady=5, sticky="nsew")
                linha_de_cartoes.append(cartao)
            self.cartoes.append(linha_de_cartoes)

    def cartao_clicado(self, linha, coluna):
        
        #Lida com o evento de clique em um cartão.

        #Args:
            #linha: A linha do cartão clicado.
            #coluna: A coluna do cartão clicado.
        
        cartao = self.cartoes[linha][coluna]
        if cartao['text'] != ' ' or len(self.cartao_revelado) == 2:
            return  # Ignora cliques em cartões já revelados ou se dois cartões já estão virados

        numero = self.grid[linha][coluna]
        cartao['text'] = numero
        self.cartao_revelado.append((linha, coluna))

        if len(self.cartao_revelado) == 2:
            self.verificar_correspondencia()

    def verificar_correspondencia(self):
        
        #Verifica se os cartões virados correspondem.

        #Se corresponderem, mantém os cartões virados, caso contrário, os esconde novamente.
        
        (linha1, coluna1), (linha2, coluna2) = self.cartao_revelado
        cartao1 = self.cartoes[linha1][coluna1]
        cartao2 = self.cartoes[linha2][coluna2]

        if self.grid[linha1][coluna1] == self.grid[linha2][coluna2]:
            if self.verificar_vitoria():
                self.exibir_mensagem_vitoria()
        else:
            self.master.after(1000, lambda: self.resetar_cartoes(cartao1, cartao2))

        self.cartao_revelado.clear()
        self.atualizar_pontuacao()

    def resetar_cartoes(self, cartao1, cartao2):
        
        #Esconde os cartões virados novamente.

        #Args:
            #cartao1: O primeiro cartão virado.
            #cartao2: O segundo cartão virado.
        
        cartao1['text'] = cartao2['text'] = ' '

    def verificar_vitoria(self):
        
        #Verifica se todos os cartões foram virados.

        #Returns:
            #bool: True se todos os cartões foram virados, False caso contrário.
        
        for linha in range(self.NUM_LINHAS):
            for coluna in range(self.NUM_COLUNAS):
                if self.cartoes[linha][coluna]['text'] == ' ':
                    return False
        return True

    def exibir_mensagem_vitoria(self):
        
        #Exibe uma mensagem de vitória ao jogador.
        
        messagebox.showinfo('Parabéns!', 'Você ganhou o jogo')
        self.master.quit()

    def atualizar_pontuacao(self):
        
        #Atualiza a pontuação do jogador e verifica se o limite de tentativas foi atingido.
        
        self.tentativas += 1
        self.label_tentativas.config(text=f"Tentativas: {self.tentativas}/{self.MAX_TENTATIVAS}")
        if self.tentativas >= self.MAX_TENTATIVAS:
            messagebox.showinfo('Fim de jogo', 'Você atingiu o limite de tentativas')
            self.master.quit()


def main():
    root = tk.Tk()
    root.title("Memory Game")
    game = JogoMemoria(root)
    
    # Calcula o tamanho ideal dos botões
    largura_botao = 100
    altura_botao = 100

    for linha in range(game.NUM_LINHAS):
        root.grid_rowconfigure(linha, weight=1, minsize=altura_botao)
    for coluna in range(game.NUM_COLUNAS):
        root.grid_columnconfigure(coluna, weight=1, minsize=largura_botao)

    root.mainloop()

if __name__ == "__main__":
    main()