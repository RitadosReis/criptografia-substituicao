alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
chave = "QWERTYUIOPASDFGHJKLZXCVBNM"


def criptografar(texto):
    resultado = ""

    for caractere in texto.upper():
        if caractere in alfabeto:
            indice = alfabeto.index(caractere)
            resultado += chave[indice]
        else:
            resultado += caractere

    return resultado


def descriptografar(texto):
    resultado = ""

    for caractere in texto.upper():
        if caractere in chave:
            indice = chave.index(caractere)
            resultado += alfabeto[indice]
        else:
            resultado += caractere

    return resultado


print("=== Cifra de Substituição Simples ===")

mensagem = input("Digite uma mensagem: ")

mensagem_cifrada = criptografar(mensagem)
mensagem_decifrada = descriptografar(mensagem_cifrada)

print("\nMensagem original:", mensagem)
print("Mensagem cifrada:", mensagem_cifrada)
print("Mensagem decifrada:", mensagem_decifrada)