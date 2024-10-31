
#função recebe uma corrida e um sistema e faz a atribuição dos pontos de cada piloto naquela corrida de acordo com o sistema informado
def analisa_corrida_sistema(corrida: list[int], sistema: list[int]) -> int:
    PONTOS = []
    ultimo_a_pontuar = sistema[0]
    for piloto in range(0,len(corrida)):
        ordem_piloto = corrida[piloto]
        if ordem_piloto<=ultimo_a_pontuar:
            PONTOS.append([(piloto+1),sistema[ordem_piloto]])
        else:
            PONTOS.append([(piloto+1),0])
    return PONTOS

#vencedor de uma dada corrida em um dado sistema (não foi usada)
def vencedor(pontos: list[list])-> list:
    piloto_pontuacao =[valor[1] for valor in pontos]
    maior_valor = max(piloto_pontuacao)
    vencedor = [piloto[0] for piloto in pontos if piloto[1]==maior_valor]
    return piloto_pontuacao,vencedor
        
#para I sistemas analisa J corridas para cada um dos corredos (parametro)
def conjunto_sistema(SISTEMAS: list[list], CORRIDAS: list[int], parametro: int)-> list:
    resultado =[]
    for S in SISTEMAS:
        a = [analisa_corrida_sistema(corrida,S) for corrida in CORRIDAS]
        resultado.append(a)

    pontuacao_final=[]
    for i in range(len(SISTEMAS)):
        
        s = 0
        for j in range (len(CORRIDAS)):
            
            a = resultado[i][j][parametro]
            for y in range(len(resultado[i][j])):
                if a[0]==resultado[i][j][y][0]:
                    s+=a[1]
        pontuacao_final.append((a[0],s,i))#recebe a posição do piloto e a soma dos seus pontos em um dado sistema
        
    return pontuacao_final



#A ordem é pode ser de N sistemas para M corridas, muito para muitos
#essa função agrupa cada uma das corridas de acordo com o sistema corrente
#Exemplo: sistema 1 - corrida 1, corrida2, sistema 2 - corrida 1, corrida2, sistema n - corrida 1, corrida2
def agrupar(L: list[list],parametro: int):
    maior = 0
    vencedor =[]
    for i in range(len(L)):
        if (L[i][parametro][1])>=maior:
            maior = (L[i][parametro][1])
            
    for i in range(len(L)):
        if (L[i][parametro][1])==maior:
            vencedor.append(L[i][parametro][0])
            
    return vencedor

'''
#Variáveis de teste

corrida1 = [1,3,4,2]
corrida2 = [4,1,3,2]


sistema1 = [3,3,2,1]
sistema2 = [3,5,4,2]
sistema3 = [3,5,4,2]

SISTEMAS = [sistema1,sistema2]
CORRIDAS = [corrida1,corrida2]
'''

#variáveis
SISTEMAS = []
CORRIDAS = []
L = []
vencedores =[]

#lógica do software
while True:
    G,P = map(int, input().split()) #recebe as duas primeiras entradas

    #condições de existência
    if G==0 and P==0:
        break
    if G<1 or G>100:
        break
    if P<1 or P>100:
        break

    #guarda o resultado de todas as corridas
    CORRIDAS = []
    for i in range(0,G):
        corrida = list(map(int,input().split()))
        CORRIDAS.append(corrida)

    #quantidade de sistemas a serem analisados
    S = int(input())

    #condição de existência
    if S<1 or S>10:
        break

    #guarda os sistemas de pontuação
    for i in range(0,S):
        sistema_pontuacao = list(map(int, input().split()))
        SISTEMAS.append(sistema_pontuacao)

    #analisa para N sistemas M corridas
    for x in range(P):
        c = conjunto_sistema(SISTEMAS,CORRIDAS,x)
        L.append(c)

    #agrupa os resultados por sitemas e indica qual/quais pilotos mais pontuaram em cada sistema de acordo com cada corrida
    for x in range(S):
        vencedores.append(agrupar(L,x))

    #zera as variáveis para assim receber as novas entradas
    SISTEMAS =[]
    CORRIDAS = []
    L =[] 

#imprimindo na tela os vencedores, cada linha representa um sistema analisado para G corridas
for linha in vencedores:
    print(linha)


