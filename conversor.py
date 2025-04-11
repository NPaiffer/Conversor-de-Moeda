def converter_moeda_simples(valor, taxa):
    return valor * taxa

def menu():
    while True:
        print()
        print()
        print()
        opcao = input()

        if opcao == "1":
            valor = float(input())
            taxa = float(input())
            resultado = converter_moeda_simples(valor, taxa)