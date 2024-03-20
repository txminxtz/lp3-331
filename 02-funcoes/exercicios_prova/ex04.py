print("Programa Eleição")

candidato1 = 0
candidato2 = 0
candidato3 = 0

numero_votos = 10

while numero_votos > 0: 
    voto = int(input("Digite seu voto entre os candidatos 1, 2 e 3: "))

    if voto == 1:
        candidato1 += 1
        numero_votos -= 1
    elif voto == 2:
        candidato2 += 1
        numero_votos -= 1
    elif voto == 3:
        candidato3 += 1
        numero_votos -= 1
    
    elif voto != 1 or voto != 2 or voto != 3:
        print("Voto invalido")

print("\nVotos no candidato 1 =", candidato1)
print("\nVotos no candidato 2 =", candidato2)
print("\nVotos no candidato 3 =", candidato3)

if candidato1 > candidato2 and candidato1 > candidato3:
    print("Candidato 1 é o vencedor!")
elif candidato2 > candidato1 and candidato2 > candidato3:
    print("Candidato 2 é o vencedor!")
elif candidato3 > candidato1 and candidato3 > candidato2:
    print("Candidato 3 é o vencedor!")
else:
    print("Houve um empate.")
