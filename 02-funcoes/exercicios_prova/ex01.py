import random

x = random.randint(1,100)

while True:
    numero = float(input("Insira um numero entre 1 e 100: "))
    
    if numero > x:
        print(f"Numero incorreto! Palpite alto")
    elif numero < x:
        print(f"Numero incorreto! Palpite baixo")
    else:
        print(f"Numero correto!")
        break

