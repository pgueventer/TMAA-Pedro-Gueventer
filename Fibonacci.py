'''
UFRJ - Universidade Federal do Rio de Janeiro

IM - Instituto de Matematica

Pedro Feteira Gueventer - 119.017.382
'''
n = int(input("Qual o valor máximo?"))
        
def soma_ímpar(limite=n):
    fn_2, fn_1, fn = 1, 1, 0
    soma = 0
    while fn < limite:
        fn_2, fn_1, fn = fn_1, fn, fn_1 + fn_2
        if fn%2 == 1:
            soma += fn
    return soma

print (soma_ímpar())
