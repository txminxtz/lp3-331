# Função
# modularizar o programa
# reuso
# manutenabilidade 

# só pode acessar se a hora estiver entre 8h e 18h
hora_atual = 12

if hora_atual >= 8 and hora_atual <= 18 :
    print('permitido o acesso')


# entrada = hora atual 
# saida se está dentro ou não do horario comercial
def dentro_horario_comercial(hora) :
    if hora_atual >= 8 and hora_atual <= 18 :
        return True 
    else: 
        return False

def denro_horario_comercial(hora_atual) :
    return hora_atual >= 8 and hora_atual <=18 

#Declaração
# def nome_função():
#   corpo da função 
#   corpo da função

# Função sem retorno
def diga_ola(nome):
    print(f"Olá (nome)")

#chamada
diga_ola('Marcos')

# Função com retorno
#Sem side efcet = Função pura
def montar_frase(nome):
    return f"Olá (nome)"

nome = Marcos 
print (montar_frase(nome))
#envia_email(montar_frase(nome))


#Paramentros e Argumentos 
#Parametros referencias que podem ser acessada 
# dentro da função
# Argumentos são os valores passados para os parametros

def somar (numero1,  numero2):
    return numero1 + numero2

somar (10.0, 5.0)

#Escopo de variaveis
#variavel local
def calcular_media(nota1, nota2, norta3) :
    media = (nota1, nota2, norta3) /3
    return media

#print(media)

#variavel global
total = 0,0

def soma ( n1 + n2 + n3 ) :
     global total
     total = n1 + n2 + n3 
     return total 

print (total)
print (1, 3, 5)
print (total) 

# parametro com valor padrão 
def boas_vindas(mensagem = 'Bom dia', nome = 'Marcos') :
    return f"(mensagem), (nome)"

print (boas_vindas ('Marcos', 'Boa noite'))
print (boas_vindas ('Marilene', 'Bom dia'))
print (boas_vindas ('Maria'))

# argumentos numerados 
print (boas_vindas(nome ='Maria'))



