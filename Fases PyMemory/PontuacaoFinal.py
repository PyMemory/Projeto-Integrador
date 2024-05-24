import Fase0Teste
import Fase1
import Fase2
import Fase4
import Fase3

class PontuacaoFinal:
    def __init__(self):
        self.ft = Fase0Teste.FaseT()
        self.f1 = Fase1.Fase1()
        self.f2 = Fase2.Fase2()
        self.f3 = Fase3.Fase3()
        self.f4 = Fase4.Fase4()
        return 
    
    def calculo_pontos(self):
        pf1 = self.f1.pontos_fase1()
        pf2 = self.f2.pontos_fase2()
        pf3 = self.f3.pontos_fase3()
        pf4 = self.f4.pontos_fase4()
        soma = pf1 + pf2 + pf3 + pf4 
        return soma
    
pontuacao_final = PontuacaoFinal()
print(pontuacao_final.calculo_pontos())