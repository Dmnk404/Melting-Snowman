import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]

def display_game_stage(mistakes, secret_word, guessed_letters):
    '''Display the current game stage.'''
    print(STAGES[mistakes])
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + ""
        else:
            display_word += "_"
    print("Word:", display_word)
    print("\n")

def play_game():

    mistakes = 0
    guessed_letters = []
    secret_word = get_random_word()
    print("Welcome to Snowman Meltdown!")
    print("Secret word selected: " + secret_word)

    while True:
        guess = input("Guess a letter: ").lower()
        if guess in guessed_letters:
            print("Already guessed this letter! Guess again.")
            continue
        print("You guessed:", guess)
        if guess in secret_word:
            guessed_letters.append(guess)
            if len(guessed_letters) == len(secret_word):
                print("Congratulations, you guessed the secret word and save the snowman!")
                break
            else:
                print("Congratulations, you guessed right")
                display_game_stage(mistakes, secret_word, guessed_letters)
        else:
            print("Sorry, you guessed wrong.")
            mistakes += 1
            display_game_stage(mistakes, secret_word, guessed_letters)
            if mistakes == 3:
                print("The secret word was:", secret_word)
                print("The snowman melted :(.")
                break



if __name__ == "__main__":
    play_game()