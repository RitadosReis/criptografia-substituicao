def cifra_cesar(texto, deslocamento):
    resultado = ""

    for caractere in texto:
        if caractere.isalpha():
            base = ord('A') if caractere.isupper() else ord('a')

            novo_caractere = chr(
                (ord(caractere) - base + deslocamento) % 26 + base
            )

            resultado += novo_caractere
        else:
            resultado += caractere

    return resultado


def decifra_cesar(texto, deslocamento):
    return cifra_cesar(texto, -deslocamento)


print("=== Cifra de César ===")

mensagem = input("Digite uma mensagem: ")
chave = int(input("Digite o valor do deslocamento: "))

mensagem_cifrada = cifra_cesar(mensagem, chave)
mensagem_decifrada = decifra_cesar(mensagem_cifrada, chave)

print("\nMensagem original:", mensagem)
print("Mensagem cifrada:", mensagem_cifrada)
print("Mensagem decifrada:", mensagem_decifrada)