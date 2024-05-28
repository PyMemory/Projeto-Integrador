import pygame
import sys
import tkinter as tk
from tkinter import * 
from tkinter import messagebox
import mysql.connector
import os

pygame.init()
pygame.mixer.init() # Inicializando a música

musica_fundo = pygame.mixer.music.load(os.path.join("assets", "musicafundo.mp3")) # Carregando a música no projeto.
musica_fundo = pygame.mixer.music.set_volume(0.4) # Número de 0 à 1.0.
musica_fundo = pygame.mixer.music.play(-1) # Colocando a música para rodar num loop.

som_clique = pygame.mixer.Sound(os.path.join("assets", "cliquebolha.mp3"))
som_ligado = True
musica_ligada = True

def tkinterfunc():

    global som_ligado

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
            cursor.execute("SELECT nomeFunc, turmaFunc FROM tb_funcionarios ORDER BY nomeFunc")
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


    # Criando a janela
    root = tk.Tk()
    root.title("Login")
    largura = 500
    altura = 300
    root.configure(bg="green")

    # Centralizando a janela na tela
    largura_screen = root.winfo_screenwidth()
    altura_screen = root.winfo_screenheight()
    posx = largura_screen/2 - largura/2
    posy = altura_screen/2 - altura/2
    root.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))

    # Rótulo Login
    my_label = Label (root, text="LOGIN", font=("Comic Sans MS", 38,), fg="white", bg="green")
    my_label.pack(pady=10)

    my_label = Label(root, text="SELECIONE O SEU NOME E SUA TURMA", font=("Helvetica", 15,), fg="white", bg="green")
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
    my_button = Button(root, text="Confirmar", activebackground="green", activeforeground="white", anchor="center", bg="systembuttonface", bd="2", default="disabled",
        disabledforeground="green", font=("Helvetica", 12), fg="green",justify="center",overrelief="raised",relief="raised",
        state="normal", takefocus=TRUE, width="10", wraplength="0")
    my_button.pack(pady=10)

    exibir_tela_login = False

    root.mainloop()

def tkinter():

    global som_ligado
    
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
        tela_teste(screen)

    # Criando a janela
    root = tk.Tk()
    root.title("Login")
    largura = 500
    altura = 300
    root.configure(bg="green")

    # Centralizando a janela na tela
    largura_screen = root.winfo_screenwidth()
    altura_screen = root.winfo_screenheight()
    posx = largura_screen/2 - largura/2
    posy = altura_screen/2 - altura/2
    root.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))

    # Rótulo Login
    my_label = Label (root, text="LOGIN", font=("Comic Sans MS", 38,), fg="white", bg="green")
    my_label.pack(pady=10)

    my_label = Label(root, text="SELECIONE O SEU NOME E SUA TURMA", font=("Helvetica", 15,), fg="white", bg="green")
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
    my_button = Button(root, text="Confirmar", activebackground="green", activeforeground="white", anchor="center", bg="systembuttonface", bd="2", default="disabled",
        disabledforeground="green", font=("Helvetica", 18), fg="green",justify="center",overrelief="raised",relief="raised",
        state="normal", takefocus=TRUE, width="10", wraplength="0", command=abrir_tela_config)
    my_button.pack(pady=10)

    root.mainloop()

def tela_teste(screen):

    largura = 1200
    altura = 671
    tela = pygame.display.set_mode((largura, altura))

    pygame.display.set_caption("Tela de Teste após o TKINTER")
    imagem = pygame.image.load(os.path.join("assets", "telalogins.png"))
    screen.blit(imagem, (0, 0))

    cor_texto = (255, 255, 255)
    
    fonte = pygame.font.Font(os.path.join("assets","RetroMario-Regular.otf"), 55)
    
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            pygame.display.flip()

def tela_config(screen):
    
    global som_ligado
    global musica_ligada

    largura = 1200
    altura = 671
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("PAINEL DE CONFIGURAÇÕES")
    imagem = pygame.image.load(os.path.join("assets", "telalogins.png"))
    screen.blit(imagem, (0, 0))

# DEFININDO CORES DOS BOTÕES E TEXTOS

    cor_botao = (0, 100, 0)  
    cor_texto = (255, 255, 255)  
    cor_botaosom = (122, 186, 120)
    cor_textosom = (0, 100, 0)

# CARREGANDO A FONTE

    fonte = pygame.font.Font(os.path.join("assets","RetroMario-Regular.otf"), 55)

# BOTÃO PARA VOLTAR PRA TELA INICIAL

    texto_botaovoltar4 = fonte.render("VOLTAR", True, cor_texto) 
    largura_botaovoltar4 = 250
    altura_botaovoltar4 = 65
    posicao_botaovoltar4 = (5, 5)
    retangulo_botaovoltar4 = pygame.Rect(posicao_botaovoltar4, (largura_botaovoltar4, altura_botaovoltar4))
    corner_radius = 20
    

# CAIXA DE TEXTO PARA IDENTIFICAÇÃO DA FUNÇÃO DE CADA BOTÃO

    texto_botaosong = fonte.render("MÚSICA", True, cor_textosom) 
    largura_botaosong = 280
    altura_botaosong = 80
    posicao_botaosong = (200, 200)
    retangulo_botaosong = pygame.Rect(posicao_botaosong, (largura_botaosong, altura_botaosong))
    corner_radius = 100

# CAIXA DE TEXTO PARA IDENTIFICAÇÃO DA FUNÇÃO DE CADA BOTÃO

    texto_botaosound = fonte.render("EFEITO SONORO", True, cor_textosom) 
    largura_botaosound = 480
    altura_botaosound = 80
    posicao_botaosound = (550, 200)
    retangulo_botaosound = pygame.Rect(posicao_botaosound, (largura_botaosound, altura_botaosound))
    corner_radius = 100

# CARREGANDO A IMAGEM DOS BOTÕES DE LIGAR E DESLIGAR MUSICA
    
    img_musica_on = pygame.image.load(os.path.join("assets", "soundon.png"))
    img_musica_off = pygame.image.load(os.path.join("assets","soundoff.png"))

    tamanho = (130, 130)

    img_musica_on = pygame.transform.scale(img_musica_on, tamanho)
    img_musica_off = pygame.transform.scale(img_musica_off, tamanho)

# CARREGANDO A IMAGEM DOS BOTÕES DE LIGAR E DESLIGAR O EFEITO SONORO

    img_efeito_on = pygame.image.load(os.path.join("assets","soundon.png"))
    img_efeito_off = pygame.image.load(os.path.join("assets","soundoff.png"))

    img_efeito_on = pygame.transform.scale(img_efeito_on, tamanho)
    img_efeito_off = pygame.transform.scale(img_efeito_off, tamanho)

    def desligar_musica():
        pygame.mixer.music.stop()

    def ligar_musica():
        pygame.mixer.music.play(-1)

    def desenhar_interface():

        tela.blit(imagem, (0, 0))
        
        # DESENHANDO OS BOTÕES NA TELA

        pygame.draw.rect(tela, cor_botao, retangulo_botaovoltar4, border_radius=corner_radius)
        texto_retangulovoltar4 = texto_botaovoltar4.get_rect(center=retangulo_botaovoltar4.center)
        tela.blit(texto_botaovoltar4, texto_retangulovoltar4)

        pygame.draw.rect(tela, cor_botaosom, retangulo_botaosong, border_radius=corner_radius)
        texto_retangulosong = texto_botaosong.get_rect(center=retangulo_botaosong.center)
        tela.blit(texto_botaosong, texto_retangulosong)

        pygame.draw.rect(tela, cor_botaosom, retangulo_botaosound, border_radius=corner_radius)
        texto_retangulosound = texto_botaosound.get_rect(center=retangulo_botaosound.center)
        tela.blit(texto_botaosound, texto_retangulosound)

        # DESENHA OS BOTÕES DE MÚSICA E DE EFEITO SONORO

        img_botao_musica = img_musica_on if musica_ligada else img_musica_off
        img_botao_efeito = img_efeito_on if som_ligado else img_efeito_off

        tela.blit(img_botao_musica, (270, 300))
        tela.blit(img_botao_efeito, (710, 300))

    exibir_tela_config = False
    exibir_main = False

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                pos_mouse = pygame.mouse.get_pos()
                if img_musica_on.get_rect(topleft=(270, 300)).collidepoint(pos_mouse):
                    som_clique.play() if som_ligado else None
                    if musica_ligada:
                        desligar_musica()
                    else:
                        ligar_musica()
                    musica_ligada = not musica_ligada
                elif img_efeito_on.get_rect(topleft=(710, 300)).collidepoint(pos_mouse):
                    som_ligado = not som_ligado
                elif retangulo_botaovoltar4.collidepoint(pos_mouse):
                    som_clique.play() if som_ligado else None
                    main(screen)
        

                
        
        
        desenhar_interface()

        pygame.display.flip()

        if exibir_tela_config:
            tela_config(screen)
            break
        elif exibir_main:
            main(screen)
            break  

def tela_login(screen):

    global som_ligado  

    largura = 1200
    altura = 671
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Tela de Login")
    imagem = pygame.image.load(os.path.join("assets","telalogins.png"))
    screen.blit(imagem, (0, 0))

    cor_botao = (0, 100, 0)  
    cor_texto = (255, 255, 255)  

    fonte = pygame.font.Font(os.path.join("assets", "RetroMario-Regular.otf"), 55)
 

#BOTÃO DE LOGIN DE ALUNO


    texto_botao3 = fonte.render("ALUNO", True, cor_texto) 
    largura_botao3 = 215
    altura_botao3 = 80
    posicao_botao3 = (500, 240)
    retangulo_botao3 = pygame.Rect(posicao_botao3, (largura_botao3, altura_botao3))
    corner_radius = 20  


#BOTÃO DE LOGIN FUNCIONÁRIO

    texto_botao4 = fonte.render("FUNCIONÁRIO", True, cor_texto) 
    largura_botao4 = 400
    altura_botao4 = 80
    posicao_botao4 = (410, 350)
    retangulo_botao4 = pygame.Rect(posicao_botao4, (largura_botao4, altura_botao4)) 
    corner_radius = 20

#BOTÃO DE VOLTAR

    texto_botaovoltar1 = fonte.render("VOLTAR", True, cor_texto) 
    largura_botaovoltar1 = 220
    altura_botaovoltar1 = 50
    posicao_botaovoltar1 = (5, 5)
    retangulo_botaovoltar1 = pygame.Rect(posicao_botaovoltar1, (largura_botaovoltar1, altura_botaovoltar1))  
    corner_radius = 20
    
    
# Desenha os botões na tela
    
    pygame.draw.rect(tela, cor_botao, retangulo_botao3, border_radius=corner_radius)
    texto_retangulo3 = texto_botao3.get_rect(center=retangulo_botao3.center)
    tela.blit(texto_botao3, texto_retangulo3)

    pygame.draw.rect(tela, cor_botao, retangulo_botao4, border_radius=corner_radius)
    texto_retangulo4 = texto_botao4.get_rect(center=retangulo_botao4.center)
    tela.blit(texto_botao4, texto_retangulo4)

    pygame.draw.rect(tela, cor_botao, retangulo_botaovoltar1, border_radius=corner_radius)
    texto_retangulovoltar1 = texto_botaovoltar1.get_rect(center=retangulo_botaovoltar1.center)
    tela.blit(texto_botaovoltar1, texto_retangulovoltar1)

   # Atualiza a tela
    pygame.display.flip()

    exibir_main = False
    exibir_tkinter = False
    exibir_tkinterfunc = False
    exibir_tela_login = False 

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if retangulo_botao3.collidepoint(evento.pos):
                    if som_ligado:
                        som_clique.play()
                    exibir_tkinter = True  
                elif retangulo_botao4.collidepoint(evento.pos):
                    if som_ligado:
                        som_clique.play()
                    exibir_tkinterfunc = True
                elif retangulo_botaovoltar1.collidepoint(evento.pos):
                    if som_ligado:
                        som_clique.play()
                    exibir_main = True
                

        pygame.display.flip()

        if exibir_main:
            main(screen)
            break
        elif exibir_tela_login:
            tela_login(screen)
            break
        elif exibir_tkinter :
            tkinter()
            break
        elif exibir_tkinterfunc:
            tkinterfunc()
            break

def main(screen):

    global som_ligado  
    
#TAMANHO DA TELA
    
    largura = 1200
    altura = 671

    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("PyMemory")
    
#CARREGANDO IMAGEM DE FUNDO
    
    imagem = pygame.image.load(os.path.join("assets","inicio.png"))

#BOTÃO DE LOGIN

    cor_botao = (0, 100, 0)  # Cor verde escuro para o botão
    cor_texto = (255, 255, 255)  # Cor branca para o texto
    
    fonte = pygame.font.Font(os.path.join("assets","RetroMario-Regular.otf"), 55)  

    texto_botao1 = fonte.render("LOGIN", True, cor_texto)  
    largura_botao1 = 190
    altura_botao1 = 80
    posicao_botao1 = (800, 65)
    retangulo_botao1 = pygame.Rect(posicao_botao1, (largura_botao1, altura_botao1))  
    corner_radius = 100
    
#BOTÃO DE CONFIG

    texto_botao2 = fonte.render("CONFIGURAÇÕES", True, cor_texto)  
    largura_botao2 = 515
    altura_botao2 = 80
    posicao_botao2 = (645, 160)
    retangulo_botao2 = pygame.Rect(posicao_botao2, (largura_botao2, altura_botao2)) 
    corner_radius = 100 


    exibir_tela_login = False
    exibir_tela_config = False

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if retangulo_botao1.collidepoint(evento.pos):
                    if som_ligado:
                        som_clique.play()
                    exibir_tela_login = True
                elif retangulo_botao2.collidepoint(evento.pos):
                    if som_ligado:
                        som_clique.play()
                    exibir_tela_config = True

                    

        tela.blit(imagem, (0, 0))

        pygame.draw.rect(tela, cor_botao, retangulo_botao1, border_radius=corner_radius)
        texto_retangulo1 = texto_botao1.get_rect(center=retangulo_botao1.center)
        tela.blit(texto_botao1, texto_retangulo1)

        pygame.draw.rect(tela, cor_botao, retangulo_botao2, border_radius=corner_radius)
        texto_retangulo2 = texto_botao2.get_rect(center=retangulo_botao2.center)
        tela.blit(texto_botao2, texto_retangulo2)


        pygame.display.flip()

        if exibir_tela_login:
            tela_login(screen)
            break
        elif exibir_tela_config:
            tela_config(screen)
            break
                        
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((1200, 671))
    main(screen)


