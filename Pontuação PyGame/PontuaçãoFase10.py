#função que armazena quantas cartas foram viradas
def cartas_viradas_por_fase10():
    
    carta_virada = ... #adicionar o método de virar a carta
    contador_viradas = 0 
    
    while(#final da fase
          ):
        
        if carta_virada == True:
            contador_viradas += 1
            
    return contador_viradas
    

#função que armazena quantas tentativas foram realizadas
def calcular_tentativas_por_fase10():
    
    tentativas = cartas_viradas_por_fase10() // 2
    
    return  tentativas

#função que calcula os pontos por fase

def calcular_pontos_fase10():
        
    tentativa = calcular_tentativas_por_fase10()
    pontuacao10 = int
    
    if tentativa <= 4:
        pontuacao10 = 10
    elif tentativa <= 8:
        pontuacao10 = 8
    elif tentativa <= 12:
        pontuacao10 = 5
    else:
        pontuacao10 = 3

    return pontuacao10