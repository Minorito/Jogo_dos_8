import copy
import math
import random
inf = 362881

class jogoOito(object):
    matriz = []
    pai = None
    g = inf
    def __init__(self, lin1, lin2, lin3):
        self.matriz = []
        self.matriz.append(lin1)
        self.matriz.append(lin2)
        self.matriz.append(lin3)
        self.pai=None
        self.g=inf
        self.f=inf
        self.h=0

    def __repr__(self):
        return f'{self.matriz}'

    def ZeroPosicao(self):
        for i in range(3):
            for j in range(3):
                if self.matriz[i][j] == 0:
                    return i, j

    def gerar_filhos(self):
        zeroPosicao = self.ZeroPosicao()
        filhos = []
        #Filho pra cima
        if(zeroPosicao[0] > 0):
            filho = copy.deepcopy(self)
            aux = filho.matriz[zeroPosicao[0]-1][zeroPosicao[1]]
            filho.matriz[zeroPosicao[0]-1][zeroPosicao[1]] = 0
            filho.matriz[zeroPosicao[0]][zeroPosicao[1]] = aux
            filhos.append(filho)
    
        #Filho pra direita
        if(zeroPosicao[1] < 2):
            filho = copy.deepcopy(self)
            aux = filho.matriz[zeroPosicao[0]][zeroPosicao[1]+1]
            filho.matriz[zeroPosicao[0]][zeroPosicao[1]+1] = 0
            filho.matriz[zeroPosicao[0]][zeroPosicao[1]] = aux
            filhos.append(filho)
    
        #Filho pra esquerda
        if(zeroPosicao[1] > 0):
            filho = copy.deepcopy(self)
            aux = filho.matriz[zeroPosicao[0]][zeroPosicao[1]-1]
            filho.matriz[zeroPosicao[0]][zeroPosicao[1]-1] = 0
            filho.matriz[zeroPosicao[0]][zeroPosicao[1]] = aux
            filhos.append(filho)

        #Filho pra baixo
        if(zeroPosicao[0] < 2):
            filho = copy.deepcopy(self)
            aux = filho.matriz[zeroPosicao[0]+1][zeroPosicao[1]]
            filho.matriz[zeroPosicao[0]+1][zeroPosicao[1]] = 0
            filho.matriz[zeroPosicao[0]][zeroPosicao[1]] = aux
            filhos.append(filho)
        return filhos

    def DFS(self):
        abertos = []
        fechados = []
        abertos.append(InitialState)
        while(len(abertos) != 0):
           estado_atual = abertos.pop()  
           if(Compara(estado_atual, GoalState)):
                for caminho in Caminho(estado_atual):
                    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in caminho.matriz]))
                    print()
                print("abertos:  ", len(abertos))
                print("fechados:  ", len(fechados))
                print("Quantidade de passos: ", estado_atual.g)
                return ("True")
           else:
                filhosDFS = estado_atual.gerar_filhos()
                fechados.append(estado_atual)
                todos_estados = abertos.copy()
                todos_estados.extend(fechados)
                for j in todos_estados:
                    for i in filhosDFS:
                        if(Compara(j, i)):
                            filhosDFS.remove(i) 
                abertos.extend(filhosDFS)
        return ("False")

    def a_estrela_eu(self):
        InitialState.g = 0
        InitialState.h = euclidiana(InitialState.matriz, GoalState.matriz)
        InitialState.f = f(InitialState.g, InitialState.h)
        abertos=[InitialState]
        fechados=[]
        while(abertos!=[]):
            estado_atual = abertos.pop(0) 
            if(Compara(estado_atual, GoalState)):
                for caminho in Caminho(estado_atual):
                    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in caminho.matriz]))
                    print()
                print("abertos:  ", len(abertos))
                print("fechados:  ", len(fechados))
                print("Quantidade de passos: ", estado_atual.g)
                return ("True", estado_atual)
            else:
                filhosA = estado_atual.gerar_filhos()
                fechados.append(estado_atual)
                todos_estados=abertos.copy()
                todos_estados.extend(fechados)
                abertos.sort(key=GmaisH)
                for j in todos_estados:
                    for i in filhosA:
                        if(Compara(j, i)):
                            filhosA.remove(i) 
                for i in filhosA:
                    i.g = estado_atual.g + 1
                    i.h = euclidiana(i.matriz, GoalState.matriz)
                    i.f = f(i.g, i.h)
                    i.pai=estado_atual
                    abertos.append(i)
        return ("False")
        
    def a_estrela_fora(self):
        InitialState.g = 0
        InitialState.h = ForaLugar(InitialState.matriz, GoalState.matriz)
        InitialState.f = f(InitialState.g, InitialState.h)
        abertos=[InitialState]
        fechados=[]
        while(abertos!=[]):
            estado_atual = abertos.pop(0) 
            if(Compara(estado_atual, GoalState)):
                for caminho in Caminho(estado_atual):
                    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in caminho.matriz]))
                    print()
                print("abertos:  ", len(abertos))
                print("fechados:  ", len(fechados))
                print("Quantidade de passos: ", estado_atual.g)
                return ("True", estado_atual)
            else:
                filhosA = estado_atual.gerar_filhos()
                fechados.append(estado_atual)
                todos_estados=abertos.copy()
                todos_estados.extend(fechados)
                abertos.sort(key=GmaisH)
                for j in todos_estados:
                    for i in filhosA:
                        if(Compara(j, i)):
                            filhosA.remove(i) 
                for i in filhosA:
                    i.g = estado_atual.g + 1
                    i.h = ForaLugar(i.matriz, GoalState.matriz)
                    i.f = f(i.g, i.h)
                    i.pai=estado_atual
                    abertos.append(i)
        return ("False")

    def gulosa(self):
        InitialState.g = 0
        InitialState.h = Manhattan(InitialState.matriz, GoalState.matriz)
        InitialState.pai = None
        abertos=[InitialState]
        fechados=[]
        while(abertos!=[]):
            estado_atual = abertos.pop(0) 
            if(Compara(estado_atual, GoalState)):
                for caminho in Caminho(estado_atual):
                    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in caminho.matriz]))
                    print()
                print("abertos:  ", len(abertos))
                print("fechados:  ", len(fechados))
                print("Quantidade de passos: ", estado_atual.g)
                return ("True", estado_atual)
            else:
                filhosA = estado_atual.gerar_filhos()
                fechados.append(estado_atual)
                todos_estados=abertos.copy()
                todos_estados.extend(fechados)
                abertos.sort(key=heuristica)
                for j in todos_estados:
                    for i in filhosA:
                        if(Compara(j, i)):
                            filhosA.remove(i) 
                for i in filhosA:
                    i.g = estado_atual.g + 1
                    i.h = Manhattan(i.matriz, GoalState.matriz)
                    i.pai=estado_atual
                    abertos.append(i)
        return ("False")

def Caminho(estado):
    camin=[]
    camin.append(estado)
    while(estado.pai!=None):
        estado=estado.pai
        camin.append(estado)
    camin.reverse()
    return camin

def NumPosicao(matriz, num):
    for i in range(3):
        for j in range(3):
            if matriz[i][j] == num:
                return i, j

def heuristica(lista):
    return lista.h

def gerar_aleatorio():
    lista = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    random.shuffle(lista)
    matriz = [lista[i::3] for i in range(3)]
    return matriz

def gerar_manual():
    matriz = []
    for i in range(3):
        linha = []
        for j in range(3):
            linha.append(int(input()))
        matriz.append(linha)
    return matriz

def GmaisH(lista):
    return lista.f

def f(g, h):
        return g + h

def Compara(valor1, valor2):
    if(valor1.matriz == valor2.matriz):
        return True
    else:
        return False

def getInv(arr):
    inv_count = 0
    vazio = 0
    for i in range(0, 9):
        for j in range(i + 1, 9):
            if arr[j] != vazio and arr[i] != vazio and arr[i] > arr[j]:
                inv_count += 1
    return inv_count

def Solucionavel(puzzle):
    inv_count = getInv([j for sub in puzzle for j in sub])
    return (inv_count % 2 == 0)
     
def Manhattan(matriz1, matrizf):
    h2=0
    for i in range(9):
        a=NumPosicao(matriz1, i)
        b=NumPosicao(matrizf, i)
        x=a[0]-b[0]
        if(x<0):
            x*=-1
        y=a[1]-b[1]
        if(y<0):
            y*=-1
        h2+=(x+y)
    return h2

def ForaLugar(matriz1, matrizf):
    h1=0
    for i in range(9):
        a=NumPosicao(matriz1, i)
        b=NumPosicao(matrizf, i)
        if(a!=b):
            h1+=1
    return h1

def euclidiana(matriz1, matriz2):
    h3=0
    for i in range(9):
        a=NumPosicao(matriz1, i)
        b=NumPosicao(matriz2, i)
        h3+=math.dist(a, b)
    return h3

#Inicio do Jogo
GoalState = jogoOito([1,2,3],[4,5,6],[7,8,0])
matriz2 = GoalState.matriz.copy()

print()
print(f'Jogo dos 8 - Minoru Takabaiashi & Samuel Piasecki')

while True:
    print()
    print(f'1 - Busca Profundidade')
    print(f'2 - Busca A* - Pecas fora do lugar')
    print(f'3 - Busca A* - Distancia Euclidiana')
    print(f'4 - Busca Gulosa - Distancia de Manhattan')
    print(f'5 - Sair do programa')

    escolha = input("Qual busca voce deseja utilizar?")

    if escolha == "1":
        print(f'1 Inserir manualmente')
        print(f'2 Gerar aleatorio')
        escolha2 = input("Qual busca voce deseja utilizar?")
        if(escolha2 == "1" ):
            matriz = gerar_manual()
            InitialState = jogoOito([0,0,0],[0,0,0],[0,0,0])
            InitialState.matriz = matriz
            puzzle = InitialState.matriz.copy()
            if(Solucionavel(puzzle)):
                print("O Jogo e Solucionavel")
                InitialState.DFS()
                print("Estado Inicial:  " , InitialState.matriz)
            else :
                print("Nao Solucionavel")
                print("Estado Inicial:  " , InitialState.matriz)
        elif(escolha2 == "2" ):
            matriz = gerar_aleatorio()
            InitialState = jogoOito([0,0,0],[0,0,0],[0,0,0])
            InitialState.matriz = matriz
            puzzle = InitialState.matriz.copy()
            if(Solucionavel(puzzle)):
                print("O Jogo e Solucionavel")
                InitialState.DFS()
                print("Estado Inicial:  " , InitialState.matriz) 
            else :
                print("Nao Solucionavel")
                print("Estado Inicial:  " , InitialState.matriz) 
    elif escolha == "2":
        print(f'1 Inserir manualmente')
        print(f'2 Gerar Aleatorio')
        escolha2 = input("Qual busca voce deseja utilizar?")
        if(escolha2 == "1" ):
            matriz = gerar_manual()
            InitialState = jogoOito([0,0,0],[0,0,0],[0,0,0])
            InitialState.matriz = matriz
            puzzle = InitialState.matriz.copy()
            if(Solucionavel(puzzle)):
                print("O Jogo e Solucionavel")
                InitialState.a_estrela_fora()
                print("Estado Inicial:  " , InitialState.matriz) 
            else :
                print("Nao Solucionavel")
                print("Estado Inicial:  " , InitialState.matriz) 
        elif(escolha2 == "2" ):
            matriz = gerar_aleatorio()
            InitialState = jogoOito([0,0,0],[0,0,0],[0,0,0])
            InitialState.matriz = matriz
            puzzle = InitialState.matriz.copy()
            if(Solucionavel(puzzle)):
                print("O Jogo e Solucionavel")
                InitialState.a_estrela_fora()
                print("Estado Inicial:  " , InitialState.matriz) 
            else :
                print("Nao Solucionavel")
                print("Estado Inicial:  " , InitialState.matriz) 
    elif escolha == "3":
        print(f'1 Inserir manualmente')
        print(f'2 Gerar aleatorio')
        escolha2 = input("Qual busca voce deseja utilizar?")
        if(escolha2 == "1" ):
            matriz = gerar_manual()
            InitialState = jogoOito([0,0,0],[0,0,0],[0,0,0])
            InitialState.matriz = matriz
            puzzle = InitialState.matriz.copy()
            if(Solucionavel(puzzle)):
                print("O Jogo e Solucionavel")
                InitialState.a_estrela_eu()
                print("Estado Inicial:  " , InitialState.matriz) 
            else :
                print("Nao Solucionavel")
                print("Estado Inicial:  " , InitialState.matriz) 
        elif(escolha2 == "2" ):
            matriz = gerar_aleatorio()
            InitialState = jogoOito([0,0,0],[0,0,0],[0,0,0])
            InitialState.matriz = matriz
            puzzle = InitialState.matriz.copy()
            if(Solucionavel(puzzle)):
                print("O Jogo e Solucionavel")
                InitialState.a_estrela_eu()
                print("Estado Inicial:  " , InitialState.matriz) 
            else :
                print("Nao Solucionavel")
                print("Estado Inicial:  " , InitialState.matriz) 
    elif escolha == "4":
        print(f'1 Inserir manualmente')
        print(f'2 Gerar aleatorio')
        escolha2 = input("Qual busca voce deseja utilizar?")
        if(escolha2 == "1" ):
            matriz = gerar_manual()
            InitialState = jogoOito([0,0,0],[0,0,0],[0,0,0])
            InitialState.matriz = matriz
            puzzle = InitialState.matriz.copy()
            if(Solucionavel(puzzle)):
                print("O Jogo e Solucionavel")
                InitialState.gulosa()
                print("Estado Inicial:  " , InitialState.matriz) 
            else :
                print("Nao Solucionavel")
                print("Estado Inicial:  " , InitialState.matriz) 
        elif(escolha2 == "2" ):
            matriz = gerar_aleatorio()
            InitialState = jogoOito([0,0,0],[0,0,0],[0,0,0])
            InitialState.matriz = matriz
            puzzle = InitialState.matriz.copy()
            if(Solucionavel(puzzle)):
                print("O Jogo e Solucionavel")
                InitialState.gulosa()
                print("Estado Inicial:  " , InitialState.matriz) 
            else :
                print("Nao Solucionavel")
                print("Estado Inicial:  " , InitialState.matriz) 
    if escolha == "5":
        break




    





    


