def verificar_num(numero):
    if numero > 0 and numero <=100:
        if numero % 2 == 0:
            return True
        
        else:
            return False
        
    else:
        print("Esse numero não está de 0 a 100")
        
numero = int(input("Digite um numero de 0 a 100:"))

resultado = verificar_num(numero)

if resultado == True:
    print(" Esse numero é par e esta entre 0 a 100")
if resultado == False:
    print("Esse numero não é par")

