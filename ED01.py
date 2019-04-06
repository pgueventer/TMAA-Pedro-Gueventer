'''
UFRJ - Universidade Federal do Rio de Janeiro

IM - Instituto de Matematica

Pedro Feteira Gueventer - 119.017.382

Diego Rodrigues Nascimento - 119.106.458

Gabriel Pedrosa Dória - 119.065.076
'''
n=3
produto_interno=0
norma1=0
norma2=0
mem_produto_interno=0
mem_norma=0
vetor_soma=0
multiesc=0
comblin=0
distância=0
ângulo=0
mem_vetor_soma=0
mem_multiesc=0
mem_comblin=0
mem_distância=0
mem_ângulo=0
import math
def main():
         global vetor_soma
         global comblin
         global norma1
         global multiesc
         global distância
         global produto_interno
         global ângulo
         global mem_produto_interno
         global mem_norma
         global mem_vetor_soma
         global mem_multiesc
         global mem_comblin
         global mem_distância
         global mem_ângulo
         print("\n\t1-Operações Vetoriais")
         print("\t2-Opções da Calculadora")
         print("\t3-Fechar o programa")
         opcao = int(input("\n\tDigite o número da opção que você deseja : "))
         if opcao == 1:
                  print("\n\t1-Soma vetorial")
                  print("\t2-Multiplicação por escalar")
                  print("\t3-Produto Interno")
                  print("\t4-Norma Vetorial(Módulo)")
                  print("\t5-Distância entre dois vetores")
                  print("\t6-Ângulo entre dois vetores")
                  print("\t7-Combinação linear de dois vetores")
                  operação = int(input("\n\tDigite o número da operação que deseja realizar : "))
                  if operação ==1:
                      mem_vetor_soma=0 
                      Soma()
                  if operação ==2:
                      mem_multi_esc=0
                      Multi()
                  if operação ==3:
                      global produto_interno
                      produto_interno = 0
                      
                      mem_produto_interno = 0
                      Produto_Interno()
                  if operação == 4:
                      global mem_norma
                      mem_norma = 0
                      global norma1
                      norma1=0
                      global norma2
                      norma2=0
                      Norma()
                  if operação == 5:
                      mem_distância=0
                      Dis()
                  if operação == 6:
                      mem_ângulo=0
                      Ang()
                  if operação == 7:
                      mem_comblin=0
                      Comb()
         elif opcao == 2:
             print("\n\t1-Alterar dimensão")
             print("\t2-Memorizar um resultado para utilizar em próximo cálculo")
             print("\t3-Acumular resultado vetorial ")
             print("\t4-Apresentar resultado vetorial")
             print("\t5-Voltar")
             operacao = int(input("\n\tDigite o número da operação que deseja realizar : "))
             if operacao == 1:
                 dimensão()
             if operacao == 2:
                 
                 print("\n\tNessa seção você pode pedir para memorizar o produto interno e a norma para que sejam usados no cálculo de ângulo entre dois vetores")
                 
                 mem_produto_interno = int(input("\n\tDigite 1 para memorizar o produto interno ou 0 para não memorizar : "))
                 if mem_produto_interno != 0:
                     Produto_Interno()
                 elif mem_produto_interno == 0:
                     main()
                 
                 mem_norma = int(input("\n\tDigite 1 para memorizar a norma ou 0 para não memorizar, caso não queira, será resetado: "))
                 if mem_norma !=0:
                     Norma()
                 else:
                     main()
             if operacao == 3:
                 mem_vetor_soma = int(input("\n\tDigite 1 para acumular o vetor soma ou 0 para não acumular.  "))
                 if mem_vetor_soma != 0:
                     Soma()
                 mem_multiesc = int(input("\n\tDigite 1 para acumular a multiplicação escalar ou 0 para não acumular.  "))
                 if mem_multiesc != 0:
                     Multi()
                 mem_produto_interno = int(input("\n\tDigite 1 para acumular o produto interno ou 0 para não acumular.  "))
                 if mem_produto_interno !=0:
                     Produto_Interno()
                 mem_norma = int(input("\n\tDigite 2 para acumular a norma ou 0 para não acumular.  "))
                 if mem_norma !=0:
                     Norma()
                 mem_distância = int(input("\n\tDigite 1 para acumular a distância ou 0 para não acumular.  "))
                 if mem_distância !=0:
                     Dis()
                 mem_ângulo = int(input("\n\tDigite 1 para acumular o ângulo ou 0 para não acumular.  "))
                 if mem_ângulo !=0:
                     Ang()
                 mem_comblin = int(input("\n\tDigite 1 para acumular a combinação linear ou 0 para não acumular.  "))
                 if mem_comblin != 0:
                     Comb()
                 main()
             if operacao == 4:
                  print("\n\t1-Soma vetorial")
                  print("\t2-Multiplicação por escalar")
                  print("\t3-Produto Interno")
                  print("\t4-Norma Vetorial(Módulo)")
                  print("\t5-Distância entre dois vetores")
                  print("\t6-Ângulo entre dois vetores")
                  print("\t7-Combinação linear de dois vetores")
                  print("OBS: Se não houver resultado acumulado, ele será apresentado como 0")
                  opresentar = int(input("\n\tDigite o número do resultado acumulado que deseja que seja apresentado : "))
                  if apresentar == 1:
                      print("\n\tO vetor soma acumulado é ({})".format(vetor_soma))
                      main()
                  if apresentar == 2:
                      print("\n\tO produto escalar acumulado é {}".format(multiesc))
                      maiin()
                  if apresentar == 3:
                      print("\n\tO produto interno acumulado é {}".format(produto_interno))
                      main()
                  if apresentar == 4:
                      print("\n\tA norma acumulada é {}".format(norma1))
                      main()
                  if apresentar == 5:
                      print("\n\tA distância acumulada é {}".format(distância))
                      main()
                  if apresentar == 6:
                      print("\n\tO ângulo acumulado é {}".format(ângulo))
                      main()
                  if apresentar == 7:
                      print("\n\tA combinação linear acunulada é {}".format(comblin))
             
             if operacao ==5:
                 main()
def dimensão():
    global n
    n = int(input("\n\tQual a dimensão que você deseja?"))
    main()             
             
def Soma():
        global vetor_soma
        v1 = input("\n\tDigite as coordenadas do Vetor 1 separadas por ',' : ").split(",")
        v2 = input("\tDigite as coordenadas do Vetor 2 separadas por ',' : ").split(",")
        soma=""
        if len(v1) != n or len(v2) != n:
            print("\n\tNúmero errado de coordenadas")
            Soma()

        for i in range(n) :
                soma += str(float(v1[i])+float(v2[i]))+","
                
        soma = soma[:-1] 
        print("\n\tO vetor soma é é: ({}).".format(soma))
        if mem_vetor_soma !=0:
            global vetor_soma
            vetor_soma = soma
        
        main()

def Multi():
    global multi_esc
    v = input("\n\tDigite as coordenadas do Vetor separadas por ',' : ").split(",")
    if len(v) != n:
            print("\n\tNúmero errado de coordenadas")
            Multi()
    m = float(input("\n\tPor quanto deseja multiplicar?"))
    produto = str()
    for i in range(n):
        x = float(v[i])
        y = m*x
        if y%1==0:
            y = int(y)
        produto += str(y)+","
        produto_final=float(produto.split(',')[:-1])
    print("\n\tO produto é ({}).".format(produto_final))
    print()
    if mem_multiesc !=0:
        multiesc = produto_final
    main()
              
def Produto_Interno():
    v1 = input("\n\tDigite as coordenadas do Vetor 1 separadas por ',' : ").split(",")
    v2 = input("\tDigite as coordenadas do Vetor 2 separadas por ',' : ").split(",")
    if len(v1) != n or len(v2) != n:
            print("\n\tNúmero errado de coordenadas")
            Produto_Interno()
    prod = 0
    for i in range(n):
        prod += float(v1[i])*float(v2[i])
    if prod % 1 == 0:
        prod = int(prod)
    print("\n\tO produto interno é {} :".format(prod))
    global mem_produto_interno
    if mem_produto_interno !=0:
        global produto_interno
        produto_interno = prod
    
def Norma():
    
    v = input("\n\tDigite as coordenadas do Vetor separadas por ',' : ").split(",")
    if len(v) != n:
            print("\n\tNúmero errado de coordenadas")
            
    norma = 0
    for i in range(n):
        norma += float(v[i])**2
    norma **=1/2
    if norma % 1 == 0:
        norma = int(norma)

    print("\n\tA norma é {}.".format(norma))

    global mem_norma
    if mem_norma !=0:
        global norma1
        norma1 = norma
        if mem_norma == 2:
            main()

        v = input("\n\tDigite as coordenadas de um 2° Vetor separadas por ',' : ").split(",")
        if len(v) != n:
            print("\n\tNúmero errado de coordenadas")
            
        norma = 0
        for i in range(n):
            norma += float(v[i])**2
        norma **=1/2
        if norma % 1 == 0:
            norma = int(norma)
        print("\n\tA norma é {}.".format(norma))
        
        if mem_norma !=0:
            global norma2
            norma2 = norma
        Ang()
    main()        
def Dis():
        global distância
        v1 = input("\n\tDigite as coordenadas do Vetor 1 separadas por ',' : ").split(",")
        v2 = input("\tDigite as coordenadas do Vetor 2 separadas por ',' : ").split(",")
        if len(v1) != n or len(v2) != n:
            print("\t\nNúmero errado de coordenadas")
            Dis()
        soma=0
        if len(v1) != n or len(v2) != n:
            print("\n\tNúmero errado de coordenadas")
            Soma()

        for i in range(n) :
                soma += (float(v1[i])-float(v2[i]))**2
        soma **= (1/2)
        print("\n\tDistância entre o Vetor 1 e o Vetor 2 é: {}.".format(soma))
        print()
        if mem_distância !=0:
            distância = soma
        main()
def Ang():
    global ângulo
    global norma1
    global norma2
    global produto_interno
    if norma1 != 0 and norma2 != 0 and produto_interno != 0:
        angulo = math.acos(produto_interno/(norma1*norma2))
        angulo = int(math.degrees(angulo))
        print("\n\tO ângulo entre os dois vetores, é aproximadamente: {}°".format(angulo))
        main()
    v1 = input("\n\tDigite as coordenadas do Vetor 1 separadas por ',' : ").split(",")
    v2 = input("\tDigite as coordenadas do Vetor 2 separadas por ',' : ").split(",")
    if len(v1) != n or len(v2) != n:
            print("\n\tNúmero errado de coordenadas")
            Ang()
    prod = 0
    ang = 0
    normaX = 0
    normaY = 0
    for i in range(n):
        prod += float(v1[i])*float(v2[i])
        normaX += float(v1[i])**2
        normaY += float(v2[i])**2
    normaX**=1/2
    normaY**=1/2
    ang = math.acos(prod/(normaX*normaY))
    ang = int(math.degrees(ang))
    print("\n\tO ângulo entre os dois vetores, é aproximadamente: {}°".format(ang))
    if mem_ângulo!=0:
        ângulo = ang
    main()
def Comb():
    global comblin
    v1 = input("\n\tDigite as coordenadas do Vetor 1 separadas por ',' : ").split(",")
    v2 = input("\tDigite as coordenadas do Vetor 2 separadas por ',' : ").split(",")
    c1 = float(input("Digite o coeficiente do primeiro vetor : "))
    c2 = float(input("Digite o coeficiente do segundo vetor : "))
    combinação = str()
    for i in range(n):
        x1 = float(v1[i])
        y1 = c1*x1
        x2 = float(v2[i])
        y2 = c2*x2
        somatório = y1+y2
        if (somatório)%1==0:
            somatório = int(somatório)
        combinação += str(somatório) +","
    print("A combinação linear dos dois vetores é igual ao vetor ({})".format(combinação[:-1]))
    combinação = combinação[:-1]
    if mem_comblin!=0:
        comblin=combinação
        
    
               
main()

