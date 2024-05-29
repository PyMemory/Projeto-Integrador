import Fases
import Operacoes
from PontuaçãoFases import Pontuacao

class FaseT:
    def __init__(self):
        self.op = Operacoes.Operacoes()
        self.jm = Fases.JogoMemoria(operacao= Operacoes.operacaoAd)
        self.pf = Pontuacao(self.jm)

    def executar_fase(self):        
        self.jm.executar()
        
    def pontos_fase0(self):
        pf0 = self.pf.pontosFase()
        print(pf0)
    
# Criar e executar a fase
faseT = FaseT()
faseT.executar_fase()


class Fase1:
    def __init__(self):
        self.jm = Fases.JogoMemoria(operacao=self.op.adicao)
        self.pf = Pontuacao(self.jm)

    def executar_fase(self):        
        self.jm.executar()
        
    def pontos_fase1(self):
        pf1 = self.pf.pontosFase()
        print(pf1)
    
# Criar e executar a fase
fase1 = Fase1()
fase1.executar_fase()
fase1.pontos_fase1()


class Fase2:
    def __init__(self):
        self.op = Operacoes.Operacoes()
        self.jm = Fases.JogoMemoria(operacao=self.op.subtracao)
        self.pf = Pontuacao(self.jm)

    def executar_fase(self):        
        self.jm.executar()

    def pontos_fase2(self):
        pf2 = self.pf.pontosFase()
        return pf2
    
# Criar e executar a fase
fase2 = Fase2()
fase2.executar_fase()
fase2.pontos_fase2()



class Fase3:
    def __init__(self):
        self.op = Operacoes.Operacoes()
        self.jm = Fases.JogoMemoria(operacao=self.op.multiplicacao)
        self.pf = Pontuacao(self.jm)

    def executar_fase(self):        
        self.jm.executar()

    def pontos_fase3(self):
        pf3 = self.pf.pontosFase()
        return pf3
    
# Criar e executar a fase
fase3 = Fase3()
fase3.executar_fase()
fase3.pontos_fase3()



class Fase4:
    def __init__(self):
        self.op = Operacoes.Operacoes()
        self.jm = Fases.JogoMemoria(operacao=self.op.divisao)
        self.pf = Pontuacao(self.jm)

    def executar_fase(self):        
        self.jm.executar()

    def pontos_fase4(self):
        pf4 = self.pf.pontosFase()
        return pf4
    
# Criar e executar a fase
fase4 = Fase4()
fase4.executar_fase()
fase4.pontos_fase4()