import tkinter
import customtkinter
import mysql.connector

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

def option_selected(*args):
    selected_option = variable.get()
    print("Opçãoo slecionada: ", selected_option)

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

janela = customtkinter.CTk()
janela.geometry("500x300")

texto = customtkinter.CTkLabel(janela, text = "Fazer Login")
texto.pack(padx=10, pady=10)

opcoes = []

