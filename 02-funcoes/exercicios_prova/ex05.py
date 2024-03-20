print("Programa Palindromo")

texto = input("Digite uma palavra ou frase: ")

def verifica_palindromo(texto):
    texto = texto.lower().replace(" ", "")
    return texto == texto [::-1]
    
if verifica_palindromo(texto):
    print(texto + " é um palindromo")
else:
    print(texto + " não é um palindromo")


