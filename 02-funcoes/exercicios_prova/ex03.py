print("Programa Calcula Vogais e Consoantes")

palavra = input("Digite uma palavra: ")

def contar_vogais_consoantes(palavra):
    vogais = 0
    consoantes = 0
    
    for char in palavra:
        if char.isalpha():
            if char.lower() in 'aeiou':
                vogais += 1
            else:
                consoantes += 1
    return vogais, consoantes

num_vogais, num_consoantes = contar_vogais_consoantes(palavra)

print("\nNumero de vogais =", num_vogais)
print("Numero de consoantes =", num_consoantes)
