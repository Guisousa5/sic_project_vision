def verificarprimo(numero):
    if numero % 2 == 0:
        print("esse numero é par")
    else:
        print("esse numero não é par")
    return

numero = int(input("Digite o numero para analise"))
verificarprimo(numero)
