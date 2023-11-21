import random 
n1 = random.randint(1,10)
meu_numero = int(input("Digite um Numero : "))

while meu_numero != n1:
    meu_numero = int(input("Digite um Numero : "))
    if meu_numero == n1:
        print("Voce Acertou!")
    else:
        print("Voce Errou !")