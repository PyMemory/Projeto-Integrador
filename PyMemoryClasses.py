import pygame
import sys
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import mysql.connector

class Tela:
    def __init__(self, app):
        self.app = app
        self.screen = app.screen

    def run(self):
        pass

class TelaConfig(Tela):
    def run(self):
        largura = 1200
        altura = 671
        tela = pygame.display.set_mode((largura, altura))

        pygame.display.set_caption("Tela de Configuração")
        imagem = pygame.image.load("telalogins.png")
        self.screen.blit(imagem, (0, 0))

        cor_botao = (0, 100, 0)
        cor_texto = (255, 255, 255)

        fonte = pygame.font.Font("RetroMario-Regular.otf", 55)

        texto_botaovoltar2 = fonte.render("VOLTAR", True, cor_texto)
        largura_botaovoltar2 = 220
        altura_botaovoltar2 = 50
        posicao_botaovoltar2 = (5, 5)
        retangulo_botaovoltar2 = pygame.Rect(posicao_botaovoltar2, (largura_botaovoltar2, altura_botaovoltar2))

        pygame.draw.rect(tela, cor_botao, retangulo_botaovoltar2)
        texto_retangulovoltar2 = texto_botaovoltar2.get_rect(center=retangulo_botaovoltar2.center)
        tela.blit(texto_botaovoltar2, texto_retangulovoltar2)

        pygame.display.flip()

        while self.app.exibir_tela_config:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.app.running = False
                    return
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    if retangulo_botaovoltar2.collidepoint(evento.pos):
                        self.app.exibir_main = True
                        self.app.exibir_tela_config = False

            pygame.display.flip()

class TelaLogin(Tela):
    def run(self):
        largura = 1200
        altura = 671
        tela = pygame.display.set_mode((largura, altura))
        pygame.display.set_caption("Tela de Login")
        imagem = pygame.image.load("telalogins.png")
        self.screen.blit(imagem, (0, 0))

        cor_botao = (0, 100, 0)
        cor_texto = (255, 255, 255)

        fonte = pygame.font.Font("RetroMario-Regular.otf", 55)

        texto_botao3 = fonte.render("ALUNO", True, cor_texto)
        largura_botao3 = 215
        altura_botao3 = 80
        posicao_botao3 = (500, 240)
        retangulo_botao3 = pygame.Rect(posicao_botao3, (largura_botao3, altura_botao3))

        texto_botao4 = fonte.render("FUNCIONÁRIO", True, cor_texto)
        largura_botao4 = 400
        altura_botao4 = 80
        posicao_botao4 = (410, 350)
        retangulo_botao4 = pygame.Rect(posicao_botao4, (largura_botao4, altura_botao4))

        texto_botaovoltar1 = fonte.render("VOLTAR", True, cor_texto)
        largura_botaovoltar1 = 220
        altura_botaovoltar1 = 50
        posicao_botaovoltar1 = (5, 5)
        retangulo_botaovoltar1 = pygame.Rect(posicao_botaovoltar1, (largura_botaovoltar1, altura_botaovoltar1))

        pygame.draw.rect(tela, cor_botao, retangulo_botao3)
        texto_retangulo3 = texto_botao3.get_rect(center=retangulo_botao3.center)
        tela.blit(texto_botao3, texto_retangulo3)

        pygame.draw.rect(tela, cor_botao, retangulo_botao4)
        texto_retangulo4 = texto_botao4.get_rect(center=retangulo_botao4.center)
        tela.blit(texto_botao4, texto_retangulo4)

        pygame.draw.rect(tela, cor_botao, retangulo_botaovoltar1)
        texto_retangulovoltar1 = texto_botaovoltar1.get_rect(center=retangulo_botaovoltar1.center)
        tela.blit(texto_botaovoltar1, texto_retangulovoltar1)

        pygame.display.flip()

        while self.app.exibir_tela_login:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.app.running = False
                    return
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    if retangulo_botao3.collidepoint(evento.pos):
                        self.app.exibir_login = True ##################
                        self.app.exibir_tela_login = False
                    elif retangulo_botao4.collidepoint(evento.pos):
                        self.app.exibir_tela_func = True
                        self.app.exibir_tela_login = False
                    elif retangulo_botaovoltar1.collidepoint(evento.pos):
                        self.app.exibir_main = True
                        self.app.exibir_tela_login = False

            pygame.display.flip()

class TelaAluno(Tela):
    def run(self):
        largura = 1200
        altura = 671
        tela = pygame.display.set_mode((largura, altura))
        pygame.display.set_caption("Tela Login Aluno")
        imagem = pygame.image.load("telalogins.png")
        self.screen.blit(imagem, (0, 0))

        cor_botao = (0, 100, 0)
        cor_texto = (255, 255, 255)

        fonte = pygame.font.Font("RetroMario-Regular.otf", 55)

        texto_botaovoltar3 = fonte.render("VOLTAR", True, cor_texto)
        largura_botaovoltar3 = 220
        altura_botaovoltar3 = 50
        posicao_botaovoltar3 = (5, 5)
        retangulo_botaovoltar3 = pygame.Rect(posicao_botaovoltar3, (largura_botaovoltar3, altura_botaovoltar3))

        pygame.draw.rect(tela, cor_botao, retangulo_botaovoltar3)
        texto_retangulovoltar3 = texto_botaovoltar3.get_rect(center=retangulo_botaovoltar3.center)
        tela.blit(texto_botaovoltar3, texto_retangulovoltar3)

        pygame.display.flip()

        while self.app.exibir_tela_aluno:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.app.running = False
                    return
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    if retangulo_botaovoltar3.collidepoint(evento.pos):
                        self.app.exibir_tela_login = True
                        self.app.exibir_tela_aluno = False

            pygame.display.flip()

class TelaFunc(Tela):
    def run(self):
        largura = 1200
        altura = 671
        tela = pygame.display.set_mode((largura, altura))
        pygame.display.set_caption("Tela Login Funcionário")
        imagem = pygame.image.load("telalogins.png")
        self.screen.blit(imagem, (0, 0))

        cor_botao = (0, 100, 0)
        cor_texto = (255, 255, 255)

        fonte = pygame.font.Font("RetroMario-Regular.otf", 55)

        texto_botaovoltar4 = fonte.render("VOLTAR", True, cor_texto)
        largura_botaovoltar4 = 220
        altura_botaovoltar4 = 50
        posicao_botaovoltar4 = (5, 5)
        retangulo_botaovoltar4 = pygame.Rect(posicao_botaovoltar4, (largura_botaovoltar4, altura_botaovoltar4))

        pygame.draw.rect(tela, cor_botao, retangulo_botaovoltar4)
        texto_retangulovoltar4 = texto_botaovoltar4.get_rect(center=retangulo_botaovoltar4.center)
        tela.blit(texto_botaovoltar4, texto_retangulovoltar4)

        pygame.display.flip()

        while self.app.exibir_tela_func:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.app.running = False
                    return
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    if retangulo_botaovoltar4.collidepoint(evento.pos):
                        self.app.exibir_tela_login = True
                        self.app.exibir_tela_func = False

            pygame.display.flip()

class TelaMain(Tela):
    def run(self):
        largura = 1200
        altura = 671
        tela = pygame.display.set_mode((largura, altura))
        pygame.display.set_caption("PyMemory")

        imagem = pygame.image.load("inicio.png")

        cor_botao = (0, 100, 0)
        cor_texto = (255, 255, 255)

        fonte = pygame.font.Font("RetroMario-Regular.otf", 55)

        texto_botao1 = fonte.render("LOGIN", True, cor_texto)
        largura_botao1 = 190
        altura_botao1 = 80
        posicao_botao1 = (800, 65)
        retangulo_botao1 = pygame.Rect(posicao_botao1, (largura_botao1, altura_botao1))

        texto_botao2 = fonte.render("CONFIGURAÇÕES", True, cor_texto)
        largura_botao2 = 480
        altura_botao2 = 80
        posicao_botao2 = (670, 160)
        retangulo_botao2 = pygame.Rect(posicao_botao2, (largura_botao2, altura_botao2))

        pygame.display.flip()

        while self.app.exibir_main:
            tela.blit(imagem, (0, 0))

            pygame.draw.rect(tela, cor_botao, retangulo_botao1)
            texto_retangulo1 = texto_botao1.get_rect(center=retangulo_botao1.center)
            tela.blit(texto_botao1, texto_retangulo1)

            pygame.draw.rect(tela, cor_botao, retangulo_botao2)
            texto_retangulo2 = texto_botao2.get_rect(center=retangulo_botao2.center)
            tela.blit(texto_botao2, texto_retangulo2)

            pygame.display.flip()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.app.running = False
                    return
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    if retangulo_botao1.collidepoint(evento.pos):
                        self.app.exibir_tela_login = True
                        self.app.exibir_main = False
                    elif retangulo_botao2.collidepoint(evento.pos):
                        self.app.exibir_tela_config = True
                        self.app.exibir_main = False

            pygame.display.flip()

class PyMemoryApp:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 671))
        self.running = True
        self.exibir_main = True
        self.exibir_tela_login = False
        self.exibir_tela_aluno = False
        self.exibir_tela_func = False
        self.exibir_tela_config = False

    def run(self):
        while self.running:
            if self.exibir_main:
                TelaMain(self).run()
            elif self.exibir_tela_login:
                TelaLogin(self).run()
            elif self.exibir_tela_aluno:
                TelaAluno(self).run()
            elif self.exibir_tela_func:
                TelaFunc(self).run()
            elif self.exibir_tela_config:
                TelaConfig(self).run()


        # Aqui você pode adicionar o código para lidar com a opção selecionada, como realizar uma consulta ao banco de dados para obter mais informações sobre a opção selecionada.

if __name__ == "__main__":
    app = PyMemoryApp()
    app.run()
