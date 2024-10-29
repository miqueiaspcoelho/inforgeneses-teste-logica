#função responsável por saber se um número é multiplo do outro
#1 - se o resultado da divisão inteira de 'n' por 'm' for 0, 'n' é multiplo de m
#2 - se for diferente de 0 'n' não é multiplo de 'm'
def multiplo(n: int, m: int)-> bool:
    if n%m==0:
        return True
    else:
        return False


#função responsável por avaliar os casos do problema
#1- se 'n' é multiplo de 3 e 5 ao mesmo tempo
#2- se 'n' é multiplo apenas de 3
#3- se 'n' é multiplo apenas de 5
#4- nenhum dos anteriores
def main()-> None:
    for n in range(1,51):
        if multiplo(n,3) and multiplo(n,5):
            print('FizzBuzz')
        elif multiplo(n,3):
            print('Fizz')
        elif multiplo(n,5):
            print('Buzz')
        else:
            print(n)
main()
