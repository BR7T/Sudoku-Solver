# criar uma matriz do tamanho da primeira casa
import random

teste = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

# vai verificar se já existe no quadrante
# se for true vai verificar se existe na linha ?????



for l in range(0,3):
    for n in range(0,3):
       teste[l][n] = random.randint(1,9)
       print(teste[l][n])
       
print(teste)

# criar mais uma matriz com a 3 matriz anteriores


            

    



    
# criar o tabuleiro final com 3 da última
#  mostrar a matriz com casas com 0