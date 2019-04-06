'''
UFRJ - Universidade Federal do Rio de Janeiro

IM - Instituto de Matematica

Pedro Feteira Gueventer - 119.017.382
'''
import time
def main():
    print("Soma dos dígitos do número X\n")
    x = 2**int(input("Qual o valor de X?"))

    a = sum(int(digit) for digit in str(x))

    print("A soma é", a,"\n")
    time.sleep(2)
    main()
    
main()
