import math

def calculaImprime(valor, potencia):
    print("Resultado:", pow(valor, potencia))

contador = 0
entrada = int(input('Digite um número: '))
opcao = int(input('Escolha uma das opções:\n1 - Cubo\n2 - Quadrado\n3 - Elevado a quarta\n0 - Sair\n'))

while(opcao != 0):

    contador += 1

    if opcao == 1:
        calculaImprime(entrada, 3)
    elif opcao == 2:
        calculaImprime(entrada, 2)
    elif opcao == 3:
        calculaImprime(entrada, 4)
    else:
        print("Você digitou uma opcão inválida.")
    
    entrada = int(input('\nDigite um número: '))
    opcao = int(input('Escolha uma das opções:\n1 - Cubo\n2 - Quadrado\n3 - Elevado a quarta\n0 - Sair\n'))

print("\nVocê encerrou o programa.")
print("\nVocê realizou", contador, "operações.")