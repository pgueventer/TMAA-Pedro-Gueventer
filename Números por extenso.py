'''
UFRJ - Universidade Federal do Rio de Janeiro
IM - Instituto de Matemática
Pedro Feteira Gueventer - 119.017.382
'''
print("Programa para retornar números por extenso de até 5 algarismos")
def main():
    start = time.time()
    unidades = ["", "um", "dois", "três", "quatro","cinco", "seis", "sete", "oito", "nove"]
    especial = ['dez', "onze", "doze", "treze", "catorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]
    dezenas = ['zero', 'dez',"vinte", "trinta", "quarenta", "cinquenta","sessenta", "setenta", "oitenta", "noventa"]
    centenas = ['zero',"cento","duzentos","trezentos","quatrocentos","quinhentos","seiscentos","setecentos","oitocentos","novecentos"]
    numero= int(input('Digite um número de até 5 algarismos : '))
    num_completo= (5-len(str(numero)))*'0'+str(numero)
    escrito=''
    contador=1
    num_adp=False
    if num_completo=='00000':
        print('zero')
    for i in num_completo:
        if contador == 1:
            if i == '1':
                escrito+=especial[int(num_completo[1])]+' mil'
                contador+=1
                num_adp= True
                continue
            if i=='0':
                contador+=1
                continue
            escrito+= dezenas[int(i)]
            contador+=1
            continue
        if contador==4:
            if i=='0':
                contador+=1
                continue
            if i == '1':
                escrito+=' e '+especial[int(num_completo[4])]
                contador+=1
                break
            escrito+= ' e '+dezenas[int(i)]
            contador+=1
            continue
        if contador==2:
            if num_adp==True:
                contador+=1
                continue
            if i=='0':
                escrito+=' mil'
                contador+=1
                continue
            escrito+=' e '+unidades[int(i)]+' mil'
            contador+=1
            continue
        if contador==3:
            if i=='0' :
                contador+=1
                continue
            if i=='1' and num_completo[3]=='0' and num_completo[4]=='0':
                escrito+= ' e cem'
                break
            escrito+=' e ' +centenas[int(i)]
            contador+=1
            continue
        if contador==5:
            if i=='0':
                contador+=1
                break
            escrito+=' e '+unidades[int(i)]
    if escrito[0:2:]==' m':
        print (escrito[7::])
    elif escrito[0:3]==' e ':
        print(escrito[3:])
    else:
        print(escrito)
    
main()
    
            
            
            
                
                
            
        
            
        
    
