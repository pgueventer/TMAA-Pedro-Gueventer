'''
UFRJ - Universidade Federal do Rio de Janeiro

IM - Instituto de Matematica

Pedro Feteira Gueventer - 119.017.382
'''


print ("Calculadora de Equações do Segundo Grau no formato de ax^2 + bx +c")

def main():
    import cmath
    import math
    import time
    a=float(input("\nQual o coeficiente 'a'?"))

    if a == 0:
        print("Coeficiente 'a' inválido para que seja uma equação do 2o grau.")
        main()
    if a != 0:
        b=float(input("\nQual o coeficiente 'b'?"))
        c=float(input("\nQual o coeficiente 'c'?"))
        d=(b**2)-(4*a*c)
        print("\nDelta =",d)

        if d > 0:
            x1 = (-b+math.sqrt(d))/(2*a)
            x2 = (-b-math.sqrt(d))/(2*a)
            print("\nEquação com duas raízes reais:",x1,"e",x2)
            time.sleep(5)
            main()

        if d == 0:
            x = -b/(2*a)
            print("\nEquação com uma raíz real", x)
            time.sleep(5)
            main()

        if d < 0:
            x1 = (-b+cmath.sqrt(d))/(2*a)
            x2 = (-b-cmath.sqrt(d))/(2*a)
            print("\nEquação com duas raízes complexas",x1,"e",x2)
            time.sleep(5)
            main()
            
        
main()    
    

