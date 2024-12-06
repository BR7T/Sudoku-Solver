# criar uma matriz do tamanho da primeira casa
import random
import time

quadrante = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

linha = [quadrante.copy() for _ in range(0,3)]

# vai verificar se já existe no quadrante
# se for true vai verificar se existe na linha ?????
def verificaSeJáExisteNoQuadrante(CasaAtual , _q): 
    temp = []
    
    for i in _q:
        for a in i:
            temp.append(a)
            print(temp)
    if temp.count(CasaAtual) > 1 :
        return False


inicio = time.time()


print("-="*32)

for col in range(0,linha.__len__()):
    for linhaquadrante in range(0 , linha[col].__len__()):
        for casa in range(0 , linha[col][linhaquadrante].__len__()):
            
            _quadrante = linha[col]
            linha[col][linhaquadrante][casa] = random.randint(1,9)
            while verificaSeJáExisteNoQuadrante(linha[col][linhaquadrante][casa] , _quadrante) == False:
                linha[col][linhaquadrante][casa] = random.randint(1,9)
    print()
print()

fim = time.time()

print("-=" * 35)
print (fim - inicio)
print(linha)



# criar mais uma matriz com a 3 matriz anteriores


            

    



    
# criar o tabuleiro final com 3 da última
#  mostrar a matriz com casas com 0