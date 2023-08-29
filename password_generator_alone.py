import random , string

def gerador_senha(tamanho_senha = 8):
    letras = string.ascii_letters
    numeros = string.digits
    pontos = string.punctuation

    lista_caracteres = letras + numeros + pontos
    senha = ""

    for i in range( 0 , tamanho_senha):
        digito = random.choice(lista_caracteres)
        senha = senha + digito

    return senha

entrada_usuario = input("Quantos digitos terá a senha?")

if  entrada_usuario.isdigit():
    entrada_usuario = int(entrada_usuario)

else:
    print("entrada invalida!")
    quit()

senha = gerador_senha(entrada_usuario)

print(f"Sua nova senha é: {senha}")



