#função que armazena quantas cartas foram viradas
def cartas_viradas_por_fase9():
    
    carta_virada = ... #adicionar o método de virar a carta
    contador_viradas = 0 
    
    while(#final da fase
          ):
        
        if carta_virada == True:
            contador_viradas += 1
            
    return contador_viradas
    

#função que armazena quantas tentativas foram realizadas
def calcular_tentativas_por_fase9():
    
    tentativas = cartas_viradas_por_fase9() // 2
    
    return  tentativas

#função que calcula os pontos por fase

def calcular_pontos_fase9():
        
    tentativa = calcular_tentativas_por_fase9()
    pontuacao9 = int
    
    if tentativa <= 4:
        pontuacao9 = 10
    elif tentativa <= 8:
        pontuacao9 = 8
    elif tentativa <= 12:
        pontuacao9 = 5
    else:
        pontuacao9 = 3
        
    return pontuacao9