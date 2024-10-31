
#função recebe uma corrida e um sistema e faz a atribuição dos pontos de cada piloto naquela corrida de acordo com o sistema informado
def analisa_corrida_sistema(corrida: list[int], sistema: list[int]) -> int:
    PONTOS = []
    ultimo_a_pontuar = sistema[0]
    for piloto in range(0,len(corrida)):
        ordem_piloto = corrida[piloto]
        if ordem_piloto<=ultimo_a_pontuar:
            #print(f'ordem do piloto = {ordem_piloto}, ultimo a pontuar = {ultimo_a_pontuar}')
            #PONTOS.append([(piloto+1),ordem_piloto,sistema[ordem_piloto]])
            PONTOS.append([(piloto+1),sistema[ordem_piloto]])
    return PONTOS

a = True
VENCEDOR = []
while a==True:
    #recebendo duas primeiras entradas G - prêmios, P - pilotos
    G,P = map(int, input().split())

    #condições de existência
    if G==0 and P==0:
        a = False
        break

    if G<1 or G>100:
        a = False
        break

    if P<1 or P>100:
        a= False
        break

    #guarda o resultado de cada corrida
    resultado_corrida =[]

    #guarda o resultado de todas as corridas
    CORRIDAS = []
    for i in range(0,G):
        corrida = list(map(int,input().split()))
        CORRIDAS.append(corrida)

    #indica a quantidade dos sistemas de pontuação
    S  = int(input())

    #condição de existência
    if S<1 or S>10:
        a= False
        break

    #guarda um sistema de pontuação
    sistema_pontuacao = []

    #guarda todos os sistemas de pontuação
    SISTEMAS = []
    for i in range(0,S):
        sistema_pontuacao = list(map(int, input().split()))
        SISTEMAS.append(sistema_pontuacao)
    #print(f'Resultados = {RESULTADOS}\nSistemas = {SISTEMAS}')

    #receberá o resultado da análise de cada corrida referente a cada sistema
    FINAL = []
    for sistema in SISTEMAS:
        #print(f'corrida = {corrida}')
        for corrida in CORRIDAS:
            #print(f'sistema = {sistema}')
            resultado = analisa_corrida_sistema(corrida,sistema)
            #FINAL.append(resultado)
            FINAL = [resultado]

        #verificação do maior ou maiores pontuadores e exibindo quem foi o piloto
        soma = 0
        maior = 0
        maiores = []
        PONTUACAO = []
        for w in CORRIDAS[0]:
            soma = 0        
            for i in range(len(FINAL)):
                for j in range(0,len(FINAL[i])):
                    if FINAL[i][j][0] == w:
                        soma+= FINAL[i][j][1]
            PONTUACAO.append((w,soma))
        #print(PONTUACAO)

        maior = PONTUACAO[0][1]
        for elemento in PONTUACAO:
            if elemento[1]>=maior:
                maior = elemento[1]
        
            #print('maior',maior,'elemento[0]',elemento[0])
        vencedor = ''
        for elemento in PONTUACAO:
            if elemento[1]==maior:
                vencedor = str(elemento[0])+' '+vencedor
        #print(vencedor)
        VENCEDOR.append(vencedor)
for item in VENCEDOR:
    print(item)

#corrida1 = [1,3,4,2]
#corrida2 = [4,1,3,2]


#sistema1 = [3,3,2,1]
#sistema2 = [3,5,4,2]

#SISTEMAS = [sistema1,sistema2]
#CORRIDAS = [corrida1,corrida2]

