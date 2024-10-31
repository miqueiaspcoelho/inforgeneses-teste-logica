'''
#recebendo duas primeiras entradas G - prêmios, P - pilotos
G,P = map(int, input().split())

#guarda o resultado de cada corrida
resultado_corrida =[]

#guarda o resultado de todas as corridas
RESULTADOS = []
for i in range(0,G):
    corrida = list(map(int,input().split()))
    RESULTADOS.append(corrida)

#indica a quantidade dos sistemas de pontuação
S  = int(input())

#guarda um sistema de pontuação
sistema_pontuacao = []

#guarda todos os sistemas de pontuação
SISTEMAS = []
for i in range(0,S):
    sistema_pontuacao = list(map(int, input().split()))
    SISTEMAS.append(sistema_pontuacao)
#print(f'Resultados = {RESULTADOS}\nSistemas = {SISTEMAS}')
'''

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

corrida1 = [1,3,4,2]
corrida2 = [4,1,3,2]


sistema1 = [3,3,2,1]
sistema2 = [3,5,4,2]

SISTEMAS = [sistema1,sistema2]
CORRIDAS = [corrida1,corrida2]

FINAL = []
for corrida in CORRIDAS:
    #print(f'corrida = {corrida}')
    for sistema in SISTEMAS:
        #print(f'sistema = {sistema}')
        resultado = analisa_corrida_sistema(corrida,sistema)
        FINAL.append(resultado)
soma = 0
PONTUACAO = []
for w in corrida1:
    soma = 0        
    for i in range(len(FINAL)):
        for j in range(0,len(FINAL[i])):
            if FINAL[i][j][0] == w:
                soma+= FINAL[i][j][1]
    PONTUACAO.append((w,soma))
print(PONTUACAO)
for f in FINAL:
    print(f)