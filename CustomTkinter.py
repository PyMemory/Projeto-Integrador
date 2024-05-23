import tkinter
import customtkinter
import mysql.connector

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

def mysql_connection(host, user, passwd, port, database=None):
    connection = mysql.connector.connect(
        host = host,
        user = user,
        passwd = passwd,
	      port = port,
        database = database
    )
    return connection

connection = mysql_connection('pi-2024-omateocortez.c.aivencloud.com','avnadmin',
                            'AVNS_mSrmiLQWmgRL7sxRVJ2', '22705', 'defaultdb')


janela = customtkinter.CTk()
janela.geometry("500x300")

def clique():
    print("Fazer Login")

texto = customtkinter.CTkLabel(janela, text = "Fazer Login")
texto.pack(padx=10, pady=10)

nome = customtkinter.CTkEntry(janela, placeholder_text="Seu nome")
nome.pack(padx=10, pady=10)

turma = customtkinter.CTkEntry(janela, placeholder_text="Sua turma")
turma.pack(padx=10, pady=10)

botao = customtkinter.CTkButton(janela, text="Confirmar", command=clique)
botao.pack(padx=10, pady=10)


janela.mainloop()


