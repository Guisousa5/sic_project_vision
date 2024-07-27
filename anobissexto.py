ano = int(input("Insira o ano para verfificarmos se é bissexto ou não"))
ano_bissexto =  (ano % 4 == 0 and ano % 100 !=0) or ano % 400 == 0
if ano_bissexto == True:
    print(" Este ano é um ano bissexto")
else:
    print("Esse ano não é um ano bissexto")
print(" ",ano_bissexto)
