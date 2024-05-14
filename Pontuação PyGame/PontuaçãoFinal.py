from PontuaçãoFase1 import calcular_pontos_fase1
from PontuaçãoFase2 import calcular_pontos_fase2
from PontuaçãoFase3 import calcular_pontos_fase3
from PontuaçãoFase4 import calcular_pontos_fase4
from PontuaçãoFase5 import calcular_pontos_fase5
from PontuaçãoFase6 import calcular_pontos_fase6
from PontuaçãoFase7 import calcular_pontos_fase7
from PontuaçãoFase8 import calcular_pontos_fase8
from PontuaçãoFase9 import calcular_pontos_fase9
from PontuaçãoFase10 import calcular_pontos_fase10


soma_pontuações = []
soma_pontuações.append(calcular_pontos_fase1())
soma_pontuações.append(calcular_pontos_fase2())                      
soma_pontuações.append(calcular_pontos_fase3())                        
soma_pontuações.append(calcular_pontos_fase4())
soma_pontuações.append(calcular_pontos_fase5())
soma_pontuações.append(calcular_pontos_fase6())
soma_pontuações.append(calcular_pontos_fase7())
soma_pontuações.append(calcular_pontos_fase8())
soma_pontuações.append(calcular_pontos_fase9())
soma_pontuações.append(calcular_pontos_fase10())
    

#função que calcular a pontuação total
def calcular_pontuacao_final():
    
    pontuacao_final = sum(soma_pontuações)

    return pontuacao_final

#função para classificar a nota final
def classificar_nota():
    mensagem = str
    
    if calcular_pontuacao_final() >= 90:
        mensagem = "Perfeita!"
    elif calcular_pontuacao_final() >= 70:
        mensagem = "Incrível!"
    elif calcular_pontuacao_final() >= 40:
        mensagem = "Ótima!"
    else:
        mensagem = "Boa!"
        
    return mensagem