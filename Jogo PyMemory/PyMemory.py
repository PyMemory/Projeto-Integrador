import pygame
import random
import tkinter as tk
from tkinter import * 
from tkinter import messagebox
import mysql.connector
import os
from Jogo import Jogo

pygame.init()
pygame.mixer.init() # Inicializando a música

musica_fundo = pygame.mixer.music.load(os.path.join("assets", "musicafundo.mp3")) # Carregando a música no projeto.
musica_fundo = pygame.mixer.music.set_volume(0.4) # Número de 0 à 1.0.
musica_fundo = pygame.mixer.music.play(-1) # Colocando a música para rodar num loop.

som_clique = pygame.mixer.Sound(os.path.join("assets", "cliquebolha.mp3"))
som_ligado = True
musica_ligada = True 

class Tela:
    def __init__(self, app):
        self.app = app
        self.screen = app.screen
    
    def run(self):
        pass

class TelaConfig(Tela):
    def run(self):
        global som_ligado
        global musica_ligada

        largura = 1200
        altura = 671
        tela = pygame.display.set_mode((largura, altura))
        pygame.display.set_caption("PAINEL DE CONFIGURAÇÕES")
        imagem = pygame.image.load(os.path.join("assets", "telalogins.png"))
        self.screen.blit(imagem, (0, 0))

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

            self.screen.blit(imagem, (0, 0))
            
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

            pygame.display.flip()

        while self.app.exibir_TelaConfig:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.app.running = False
                    return
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
                        self.app.exibir_Inicio = True
                        self.app.exibir_TelaConfig = False

            
            desenhar_interface()

            pygame.display.flip()

class Inicio(Tela):
    def run(self):

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

        texto_botao1 = fonte.render("JOGAR", True, cor_texto)  
        largura_botao1 = 215
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

    #BOTÃO DE TUTORIAL

        texto_botao3 = fonte.render("TUTORIAL", True, cor_texto)
        largura_botao3 = 330
        altura_botao3 = 80
        posicao_botao3 = (730, 260)
        retangulo_botao3 = pygame.Rect(posicao_botao3, (largura_botao3, altura_botao3)) 
        corner_radius = 100


        while self.app.exibir_Inicio:

            tela.blit(imagem, (0, 0))

            pygame.draw.rect(tela, cor_botao, retangulo_botao1, border_radius=corner_radius)
            texto_retangulo1 = texto_botao1.get_rect(center=retangulo_botao1.center)
            tela.blit(texto_botao1, texto_retangulo1)

            pygame.draw.rect(tela, cor_botao, retangulo_botao2, border_radius=corner_radius)
            texto_retangulo2 = texto_botao2.get_rect(center=retangulo_botao2.center)
            tela.blit(texto_botao2, texto_retangulo2)

            pygame.draw.rect(tela, cor_botao, retangulo_botao3, border_radius=corner_radius)
            texto_retangulo3 = texto_botao3.get_rect(center=retangulo_botao3.center)
            tela.blit(texto_botao3, texto_retangulo3)

            pygame.display.flip()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.app.running = False
                    return
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    if retangulo_botao1.collidepoint(evento.pos):
                        Jogo.jogo()
                        self.app.exibir_Inicio = False
                        if som_ligado:
                            som_clique.play()
                    elif retangulo_botao2.collidepoint(evento.pos):
                        self.app.exibir_TelaConfig = True
                        self.app.exibir_Inicio = False
                        if som_ligado:
                            som_clique.play()
                    elif retangulo_botao3.collidepoint(evento.pos):
                        self.app.exibir_TelaTutorial = True
                        self.app.exibir_Inicio = False
                        if som_ligado:
                            som_clique.play()

            pygame.display.flip()

class TelaTutorial(Tela):
    def run(self):
        global som_ligado
        global musica_ligada

        largura = 1200
        altura = 671
        tela = pygame.display.set_mode((largura, altura))
        pygame.display.set_caption("TUTORIAL PYMEMORY")
        imagem = pygame.image.load(os.path.join("assets", "tutorial.png"))
        self.screen.blit(imagem, (0, 0))

        cor_botao = (0, 100, 0)  
        cor_texto = (255, 255, 255)  
        
        fonte = pygame.font.Font(os.path.join("assets","RetroMario-Regular.otf"), 55)

        texto_botaovoltar = fonte.render("VOLTAR", True, cor_texto) 
        largura_botaovoltar = 250
        altura_botaovoltar = 65
        posicao_botaovoltar = (5, 5)
        retangulo_botaovoltar = pygame.Rect(posicao_botaovoltar, (largura_botaovoltar, altura_botaovoltar))
        corner_radius = 100


        pygame.draw.rect(tela, cor_botao, retangulo_botaovoltar, border_radius=corner_radius)
        texto_retangulovoltar = texto_botaovoltar.get_rect(center=retangulo_botaovoltar.center)
        tela.blit(texto_botaovoltar, texto_retangulovoltar)


        pygame.display.flip()
        
        while self.app.exibir_TelaTutorial:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.app.running = False
                    return
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    pos_mouse = pygame.mouse.get_pos()
                    if retangulo_botaovoltar.collidepoint(pos_mouse):
                        som_clique.play() if som_ligado else None
                        self.app.exibir_Inicio = True
                        self.app.exibir_TelaTutorial = False
                    
        
            pygame.display.flip()

class PyMemoryApp:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200,671))
        self.running = True
        self.exibir_Inicio = True
        self.exibir_TelaConfig = False
        self.exibir_TelaTutorial = False

    def run(self):
        while self.running:
            if self.exibir_Inicio:
                Inicio(self).run()
            elif self.exibir_TelaConfig:
                TelaConfig(self).run()
            elif self.exibir_TelaTutorial:
                TelaTutorial(self).run()

    def stop(self):
        self.running = False
                   
if __name__ == "__main__":
    app = PyMemoryApp()
    app.run()
    
    

