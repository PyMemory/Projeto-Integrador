import tkinter as tk
from tkinter import messagebox
import mysql.connector
import pygame
import sys

# Função da tela de configuração (Pygame)
def tela_config():
    pygame.init()
    largura = 1200
    altura = 671
    tela = pygame.display.set_mode((largura, altura))

    pygame.display.set_caption("Tela de Configuração")
    imagem = pygame.image.load("telalogins.png")
    tela.blit(imagem, (0, 0))

    cor_texto = (255, 255, 255)

    fonte = pygame.font.Font("RetroMario-Regular.otf", 55)

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                

            pygame.display.flip()

# Função da tela inicial (Tkinter)
def tkinter():
    def option_selected(*args):
        selected_option = variable.get()
        # Aqui você pode adicionar o código para lidar com a opção selecionada, como realizar uma consulta ao banco de dados para obter mais informações sobre a opção selecionada.

    def carregar_opcoes():
        try:
            # Conectando ao banco de dados
            conexao = mysql.connector.connect(
                host="pi-2024-omateocortez.c.aivencloud.com",
                port="22705",
                user="avnadmin",
                password="AVNS_6u-r-XwHHM_Ryaqe3ZP",
                database="PyMemoryDB"
            )

            cursor = conexao.cursor()

            # Consulta SQL para selecionar os nomes dos alunos e suas turmas da tabela tb_alunos
            cursor.execute("SELECT nomeAluno, turmaAluno FROM tb_alunos ORDER BY turmaAluno")
            resultado = cursor.fetchall()

            # Atualizando as opções no menu suspenso com os nomes dos alunos e suas turmas
            opcoes.clear()
            for row in resultado:
                opcao = f"{row[0]} - {row[1]}"  # Concatenando o nome do aluno e sua turma
                opcoes.append(opcao)

            variable.set(opcoes[0])

            cursor.close()
            conexao.close()

        except mysql.connector.Error as error:
            messagebox.showerror("Erro", f"Erro ao conectar ao banco de dados: {error}")

    def abrir_tela_config():
        root.destroy()
        tela_config()

    # Criando a janela
    root = tk.Tk()
    root.title("Login")
    largura = 500
    altura = 300
    root.configure(bg="green")

    # Centralizando a janela na tela
    largura_screen = root.winfo_screenwidth()
    altura_screen = root.winfo_screenheight()
    posx = largura_screen / 2 - largura / 2
    posy = altura_screen / 2 - altura / 2
    root.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))

    # Rótulo Login
    my_label = tk.Label(root, text="LOGIN", font=("Comic Sans MS", 38,), fg="white", bg="green")
    my_label.pack(pady=10)

    my_label = tk.Label(root, text="SELECIONE O SEU NOME E SUA TURMA", font=("Helvetica", 15,), fg="white", bg="green")
    my_label.pack(pady=10)

    # Permitindo o redimensionamento horizontal, mas não vertical
    root.resizable(False, False)

    # Lista vazia para armazenar as opções do menu suspenso
    opcoes = []

    # Variável para armazenar a opção selecionada
    variable = tk.StringVar(root)

    # Carregar as opções do banco de dados
    carregar_opcoes()

    # Criar o menu suspenso
    dropdown = tk.OptionMenu(root, variable, *opcoes)
    dropdown.pack(pady=10)
    dropdown.config(font=("Helvetica", 20))  # Muda o tamanho da fonte

    # Definir uma função a ser chamada quando uma opção for selecionada
    variable.trace("w", option_selected)

    # Botão de Confirmar
    my_button = tk.Button(root, text="Confirmar", activebackground="green", activeforeground="white", anchor="center",
                          bg="systembuttonface", bd="2", default="disabled",
                          disabledforeground="green", font=("Helvetica", 12), fg="green", justify="center",
                          overrelief="raised", relief="raised",
                          state="normal", takefocus=True, width="10", wraplength="0", command=abrir_tela_config)
    my_button.pack(pady=10)

    root.mainloop()

# Iniciar a aplicação Tkinter
tkinter()