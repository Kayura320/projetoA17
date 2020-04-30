#jogo dos dados 
import random

dado1 = int(random.randrange(1,6))
dado2 = int(random.randrange(1,6))
resultado = dado1+dado2
aposta = int(input("Digite sua aposta: "))

print("E a soma dos dados é....",resultado)
if aposta == resultado:
    print("Você acertou!!!")
else:
    print("Que pena, não foi dessa vez")
