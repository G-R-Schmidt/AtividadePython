import random

def escolher_palavra():
    with open("lista_palavras.txt", "r") as arquivo:
        palavras = arquivo.readlines()
    return random.choice(palavras).strip().lower()

def jogo_adivinhacao():
    palavra = escolher_palavra()
    letras_reveladas = ["_"] * len(palavra)
    letras_usadas = []

    tentativas_restantes = 6

    print("Bem-vindo ao Jogo da Adivinhação de Palavras!")
    print(f"A palavra tem {len(palavra)} letras.")

    while tentativas_restantes > 0:
        print("\nPalavra: " + " ".join(letras_reveladas))
        print("Letras usadas: " + ", ".join(letras_usadas))
        print(f"Tentativas restantes: {tentativas_restantes}")

        tentativa = input("Digite uma letra: ").strip().lower()

        if len(tentativa) != 1 or not tentativa.isalpha():
            print("Por favor, insira uma única letra válida.")
            continue

        if tentativa in letras_usadas:
            print("Você já usou esta letra antes.")
            continue

        letras_usadas.append(tentativa)

        if tentativa in palavra:
            for i in range(len(palavra)):
                if palavra[i] == tentativa:
                    letras_reveladas[i] = tentativa
        else:
            tentativas_restantes -= 1

        if "_" not in letras_reveladas:
            print("\nParabéns! Você adivinhou a palavra: " + palavra)
            break

    if "_" in letras_reveladas:
        print("\nVocê perdeu! A palavra era: " + palavra)

if __name__ == "__main__":
    jogo_adivinhacao()
