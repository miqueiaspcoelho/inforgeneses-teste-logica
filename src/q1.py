#função responsável por saber se um número é multiplo do outro
def multiplo(n: int, m: int)-> bool:
    if n%m==0:
        return True
    else:
        return False

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
