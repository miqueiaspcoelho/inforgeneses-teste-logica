'''
Função para calcular a sequência de Fibonacci

- Definição da sequência de Fibonacci a(i+1) = a(i-1) + a(i-2)
--Variáveis--
a0 = 0 e a1=1
próximo = a0 + a1
a0 e a1 estão sempre sendo ajustados a cada novo cálculo, recebendo seus sucessores na sequência
sequencia_calculada irá guardar os n-2 valores da sequência, pois, a0 e a1 são adicionados no inicio

--Casos possíveis para n:int--
Caso 1: o número avaliado por fib é maior que 2
Caso 2: o número avaliado por fib é igual a 2
Caso 3: o número avaliado por fib é igual a 1
Caso 4: nenhum dos anteriores
'''

def fib(n: int)-> int:
    a0 = 0 
    a1 = 1
    proximo='' 
    sequencia_calculada = [] 
    sequencia_calculada.append(a0)
    sequencia_calculada.append(a1)
    
    if n>2:
        for x in range(0,n-2): 
            proximo = a0 + a1
            a0 = a1 
            a1 = proximo
            sequencia_calculada.append(proximo)
    elif n==2:
        sequencia_calculada = [0,1]
    elif n==1:
        sequencia_calculada = [0]
    else:
        sequencia_calculada = []
    
    return sequencia_calculada
    
def main():
    sequencia_fibonacci = fib(40)
    for n in sequencia_fibonacci:
        print(n)
main()