import random

def choose_word():
    words = ['Stranger Things', 'Coringa', 'Jurassic Park', 'Vingadores', 'Clube da Luta', 'Avatar', 'Peaky Blinders']
    return random.choice(words).lower()

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter.lower() in guessed_letters or letter == ' ':
            display += letter
        else:
            display += '_'
    return display

def desenha_forca(erros):
    print("   _______     ")
    print("  |/      |    ")

    if(erros == 1):
        print("  |      (_)   ")
        print("  |            ")
        print("  |            ")
        print("  |            ")

    if(erros == 2):
        print("  |      (_)   ")
        print("  |      \     ")
        print("  |            ")
        print("  |            ")

    if(erros == 3):
        print("  |      (_)   ")
        print("  |      \|    ")
        print("  |            ")
        print("  |            ")

    if(erros == 4):
        print("  |      (_)   ")
        print("  |      \|/   ")
        print("  |            ")
        print("  |            ")

    if(erros == 5):
        print("  |      (_)   ")
        print("  |      \|/   ")
        print("  |       |    ")
        print("  |            ")

    if(erros == 6):
        print("  |      (_)   ")
        print("  |      \|/   ")
        print("  |       |    ")
        print("  |      /     ")

    if (erros == 7):
        print("  |      (_)   ")
        print("  |      \|/   ")
        print("  |       |    ")
        print("  |      / \   ")

    print("  |            ")
    print(" _|___         ")
    print()

def play_game():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 7
    erros = 0

    print("Bem-vindo ao Jogo da Forca!")
    print(display_word(word_to_guess, guessed_letters))

    while True:
        desenha_forca(erros)
        guess = input("Digite uma letra: ").lower()

        if guess in guessed_letters:
            print("Voce ja tentou esta letra. Tente outra.")
        elif guess in word_to_guess:
            guessed_letters.append(guess)
            print(display_word(word_to_guess, guessed_letters))
            if '_' not in display_word(word_to_guess, guessed_letters):
                print("Parabens! Voce acertou a palavra:", word_to_guess)
                break
        else:
            erros += 1
            attempts -= 1
            print("Letra incorreta! Voce tem {} tentativas restantes.".format(attempts))
            if erros == 7:
                print("Voce perdeu! A palavra correta era:", word_to_guess)
                break

play_game()
