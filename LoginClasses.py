import tkinter as tk
from tkinter import *
from tkinter import messagebox
import mysql.connector

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.largura = 500
        self.altura = 300
        self.root.configure(bg="green")

        # Centralizando a janela na tela
        largura_screen = self.root.winfo_screenwidth()
        altura_screen = self.root.winfo_screenheight()
        posx = largura_screen / 2 - self.largura / 2
        posy = altura_screen / 2 - self.altura / 2
        self.root.geometry(f"{self.largura}x{self.altura}+{int(posx)}+{int(posy)}")

        self.create_widgets()

    def create_widgets(self):
        # Rótulo Login
        my_label = Label(self.root, text="LOGIN", font=("Comic Sans MS", 38), fg="white", bg="green")
        my_label.pack(pady=10)

        my_label = Label(self.root, text="SELECIONE O SEU NOME E SUA TURMA", font=("Helvetica", 15), fg="white", bg="green")
        my_label.pack(pady=10)

        # Permitindo o redimensionamento horizontal, mas não vertical
        self.root.resizable(False, False)

        # Lista vazia para armazenar as opções do menu suspenso
        self.opcoes = []

        # Variável para armazenar a opção selecionada
        self.variable = tk.StringVar(self.root)

        # Carregar as opções do banco de dados
        self.carregar_opcoes()

        # Criar o menu suspenso
        self.dropdown = tk.OptionMenu(self.root, self.variable, *self.opcoes)
        self.dropdown.pack(pady=10)
        self.dropdown.config(font=("Helvetica", 20))  # Muda o tamanho da fonte

        # Definir uma função a ser chamada quando uma opção for selecionada
        self.variable.trace("w", self.option_selected)

        # Botão de Confirmar 
        my_button = Button(self.root, text="Confirmar",
                           activebackground="green",
                           activeforeground="white",
                           anchor="center",
                           bg="systembuttonface",
                           bd="2",
                           default="disabled",
                           disabledforeground="green",
                           font=("Helvetica", 12),
                           fg="green",
                           state="normal",
                           takefocus=TRUE,
                           width="10",
                           wraplength="0"
                           )
        my_button.pack(pady=10)

    def carregar_opcoes(self):
        try:
            # Conectando ao banco de dados
            conexao = mysql.connector.connect(
                host="pi-2024-omateocortez.c.aivencloud.com",
                port="22705",
                user="avnadmin",
                password="AVNS_mSrmiLQWmgRL7sxRVJ2",
                database="PyMemoryDB"
            )

            cursor = conexao.cursor()

            # Consulta SQL para selecionar os nomes dos alunos e suas turmas da tabela tb_alunos
            cursor.execute("SELECT nomeAluno, turmaAluno FROM tb_alunos ORDER BY turmaAluno")
            resultado = cursor.fetchall()

            # Atualizando as opções no menu suspenso com os nomes dos alunos e suas turmas
            self.opcoes.clear()
            for row in resultado:
                opcao = f"{row[0]} - {row[1]}"  # Concatenando o nome do aluno e sua turma
                self.opcoes.append(opcao)

            self.variable.set(self.opcoes[0])

            cursor.close()
            conexao.close()

        except mysql.connector.Error as error:
            messagebox.showerror("Erro", f"Erro ao conectar ao banco de dados: {error}")

    def option_selected(self, *args):
        selected_option = self.variable.get()
        # Aqui você pode adicionar o código para lidar com a opção selecionada, como realizar uma consulta ao banco de dados para obter mais informações sobre a opção selecionada.

if __name__ == "__main__":
    root = tk.Tk()
    app = Login(root)
    root.mainloop()