# Criando um jogo da forca simples em Python
import random

def escolher_palavra():
    palavras = ["banana", "abacaxi", "laranja", "morango", "uva", "melancia"]
    return random.choice(palavras)

def jogar_forca():
    palavra = escolher_palavra()
    letras_adivinhadas = set()
    tentativas = 6
    palavra_oculta = ['_'] * len(palavra)

    print("Bem-vindo ao jogo da Forca!")
    
    while tentativas > 0 and '_' in palavra_oculta:
        print("\nPalavra: " + ' '.join(palavra_oculta))
        print(f"Tentativas restantes: {tentativas}")
        letra = input("Adivinhe uma letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, insira uma única letra.")
            continue

        if letra in letras_adivinhadas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        letras_adivinhadas.add(letra)

        if letra in palavra:
            for idx, char in enumerate(palavra):
                if char == letra:
                    palavra_oculta[idx] = letra
            print("Boa! Você acertou uma letra.")
        else:
            tentativas -= 1
            print("Letra incorreta.")

    if '_' not in palavra_oculta:
        print(f"Parabéns! Você adivinhou a palavra: {palavra}")
    else:
        print(f"Você perdeu! A palavra era: {palavra}")

jogar_forca()
