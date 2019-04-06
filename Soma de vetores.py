'''
UFRJ - Universidade Federal do Rio de Janeiro

IM - Instituto de Matematica

Pedro Feteira Gueventer - 119.017.382
'''
print("Vetor soma da soma de dois vetores")
def main():
        v1 = input("\n\tDigite as coordenadas do Vetor 1 separadas por ',' : ").split(",")
        v2 = input("\tDigite as coordenadas do Vetor 2 separadas por ',' : ").split(",")
        soma=""
        

        for i in range(len(v1)) :
                soma += str(float(v1[i])+float(v2[i]))+","
                
        soma = soma[:-1] 
        print("\n\tO vetor soma é é: ({}).".format(soma))
main()
