#par ou impar

print("Nos encontramos novamente não é mesmo? haha")
print("Prepare-se eu te desafio para um jogo de par ou ímpar")
import random
impar = 1
par = 2
oponenteE = int(random.randrange(1,2))
if oponenteE == impar:
    print("Seu adversário escolheu ímpar, você será o par")
    suaEscolha = int(input("Escolha o número que vai utilizar: "))
    oponente = int(random.randrange(1,5))
    print("seu adversário escolheu: ",oponente)
    if (oponente + suaEscolha)%2 == 0:
        print("Você venceu dessa vez.. na próxima eu serei o vencedor!")
    else:
        print("Hahahaha! a vitória é minha!!")
else:
    print("Seu adversário escolheu par, você será o ímpar")
    suaEscolha = int(input("Escolha o número que vai utilizar: "))
    oponente = int(random.randrange(1,5))
    print("seu adversário escolheu: ",oponente)
    if (oponente + suaEscolha)%2 != 0:
        print("Você venceu dessa vez.. na próxima eu serei o vencedor!")
    else:
        print("Hahahaha! a vitória é minha!!")

                
               
