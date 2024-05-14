#função que armazena quantas cartas foram viradas
def cartas_viradas_por_fase6():
    
    carta_virada = ... #adicionar o método de virar a carta
    contador_viradas = 0 
    
    while(#final da fase
          ):
        
        if carta_virada == True:
            contador_viradas += 1
            
    return contador_viradas
    

#função que armazena quantas tentativas foram realizadas
def calcular_tentativas_por_fase6():
    
    tentativas = cartas_viradas_por_fase6() // 2
    
    return  tentativas

#função que calcula os pontos por fase

def calcular_pontos_fase6():
        
    tentativa = calcular_tentativas_por_fase6()
    pontuacao6 = int
    
    if tentativa <= 4:
        pontuacao6 = 10
    elif tentativa <= 8:
        pontuacao6 = 8
    elif tentativa <= 12:
        pontuacao6 = 5
    else:
        pontuacao6 = 3
    
    return pontuacao6