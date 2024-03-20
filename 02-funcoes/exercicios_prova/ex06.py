print("Programa Notas Escolares")

nota = float(input("Digite a nota de 0 a 100: "))

if nota < 0 or nota > 100:
    print("Nota inválida. Por favor, insira uma nota entre 0 e 100.")
else:
    if nota < 20:
        print("Nota F")
    elif nota < 30:
        print("Nota D-")
    elif nota < 40:
        print("Nota D")
    elif nota < 45:
        print("Nota D+")
    elif nota < 50:
        print("Nota C-")
    elif nota < 60:
        print("Nota C")
    elif nota < 65:
        print("Nota C+")
    elif nota < 70:
        print("Nota B-")
    elif nota < 80:
        print("Nota B")
    elif nota < 85:
        print("Nota B+")
    elif nota < 90:
        print("Nota A-")
    elif nota < 100:
        print("Nota A")
    else:
        print("Nota A+")
