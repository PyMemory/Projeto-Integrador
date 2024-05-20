import tkinter as tk
from tkinter import messagebox
import mysql.connector

def option_selected(*args):
    selected_option = variable.get()
    print("Opção selecionada:", selected_option)

    # Aqui você pode adicionar o código para lidar com a opção selecionada, como realizar uma consulta ao banco de dados para obter mais informações sobre a opção selecionada.

def carregar_opcoes():
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

        # Consulta SQL para selecionar os nomes dos funcionários e suas turmas da tabela tb_funcionarios
        cursor.execute("SELECT nomeFunc, turmaFunc FROM tb_funcionarios ORDER BY nomeFunc")
        resultado = cursor.fetchall()

        # Atualizando as opções no menu suspenso com os nomes dos funcionários e suas turmas
        opcoes.clear()
        for row in resultado:
            opcao = f"{row[0]} - {row[1]}"  # Concatenando o nome do funcionário e sua turma
            opcoes.append(opcao)

        variable.set(opcoes[0])

        cursor.close()
        conexao.close()

    except mysql.connector.Error as error:
        messagebox.showerror("Erro", f"Erro ao conectar ao banco de dados: {error}")

# Criando a janela
root = tk.Tk()
root.title("Menu Suspenso com Nome do Aluno e Turma Ordenados")

# Permitindo o redimensionamento horizontal, mas não vertical
root.resizable(True, False)

# Lista vazia para armazenar as opções do menu suspenso
opcoes = []

# Variável para armazenar a opção selecionada
variable = tk.StringVar(root)

# Carregar as opções do banco de dados
carregar_opcoes()

# Criar o menu suspenso
dropdown = tk.OptionMenu(root, variable, *opcoes)
dropdown.pack(pady=10)

# Definir uma função a ser chamada quando uma opção for selecionada
variable.trace("w", option_selected)

# Exibir a janela
root.mainloop()
