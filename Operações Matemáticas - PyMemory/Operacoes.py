import random

class Operacoes():
    
    def adicao(self):
        x = random.randint(0, 20)
        y = random.randint(0, 20)
        resposta = x + y
        respostai = y + x
        if x >= y:
            return x, y, resposta
        else:
            return y, x, respostai
        
    
    def subtracao(self):
        x = random.randint(0, 20)
        y = random.randint(0, 20)
        resposta = x - y
        respostai = y - x
        if x >= y:
            return x, y, resposta
        else:
            return y, x, respostai
        
    
    def multiplicacao(self):
        x = random.randint(0, 10)
        y = random.randint(0, 10)
        resposta = x * y
        respostai = y * x
        if x >= y:
            return x, y, resposta
        else:
            return y, x, respostai
        
        
    def divisao(self):
        x = random.randint(1, 30)
        # Encontrar os divisores de x dentro do intervalo de 1 a 20 (faz com que os resultados sejam apenas Inteiros)
        divisores = [i for i in range(1, 21) if x % i == 0]

        # Selecionar um divisor aleatório
        if divisores:
            y = random.choice(divisores)
        else:
            y = None
            
        resposta = x // y
        
        return x, y, resposta   