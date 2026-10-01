# Atividade - Algoritmos de Substituição

Este projeto apresenta duas implementações práticas de algoritmos clássicos de criptografia por substituição utilizando Python:

- Cifra de César
- Cifra de Substituição Simples

O objetivo da atividade é demonstrar, na prática, como diferentes técnicas de substituição podem ser utilizadas para transformar uma mensagem original em uma mensagem cifrada.

## 1. Cifra de César

A Cifra de César é um algoritmo clássico de substituição que desloca cada letra do alfabeto por uma quantidade fixa de posições.

Exemplo com deslocamento 3:

A → D
B → E
C → F

Assim, a palavra:

CASA

se transforma em:

FDVD

No programa, o usuário informa:

1. A mensagem que deseja criptografar.
2. O valor do deslocamento.

O programa realiza a criptografia e, em seguida, a descriptografia da mensagem.

### Exemplo

Mensagem original:

SEGURANCA

Chave:

3

Mensagem cifrada:

VHJXUDQFD

Mensagem decifrada:

SEGURANCA

Arquivo utilizado:

`caesar_cipher.py`

---

## 2. Cifra de Substituição Simples

Na Cifra de Substituição Simples, cada letra do alfabeto é substituída por outra letra de acordo com uma chave previamente definida.

Neste projeto foi utilizada a seguinte associação:

```text
ABCDEFGHIJKLMNOPQRSTUVWXYZ
QWERTYUIOPASDFGHJKLZXCVBNM