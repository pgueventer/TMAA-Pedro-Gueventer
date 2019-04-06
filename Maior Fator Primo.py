'''
UFRJ - Universidade Federal do Rio de Janeiro

IM - Instituto de Matematica

Pedro Feteira Gueventer - 119.017.382
'''
print("Maior fator primo de 3852914583882 é:")

import math 
  

def maiorFatorPrimo (n): 
      
 
    maiorPrimo = -1
      
    
    while n % 2 == 0: 
        maiorPrimo = 2
        n >>= 1     
          
   
    for i in range(3, int(math.sqrt(n)) + 1, 2): 
        while n % i == 0: 
            maiorPrimo = i 
            n = n / i 
      
    
    if n > 2: 
        maiorPrimo = n 
      
    return int(maiorPrimo) 
  

n = 3852914583882
print(maiorFatorPrimo(n)) 
  

