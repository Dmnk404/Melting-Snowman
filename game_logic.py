import random
from ascii_art import STAGES
from colorama import Fore, Style, init

# Initiiere colorama (besonders wichtig für Windows-Terminals)
init(autoreset=True)

WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    return random.choice(WORDS)


def display_game_stage(mistakes, secret_word, guessed_letters):
    print(STAGES[mistakes])
    display_word = " ".join(
        [letter if letter in guessed_letters else "_" for letter in secret_word]
    )
    print(f"\n🔤 {Fore.YELLOW}Word:{Style.RESET_ALL} {display_word}")
    print(f"📚 {Fore.CYAN}Guessed letters:{Style.RESET_ALL} {' '.join(sorted(guessed_letters))}")
    print(f"❌ {Fore.RED}Mistakes:{Style.RESET_ALL} {mistakes} of 3")
    print("-" * 30)


def play_game():
    mistakes = 0
    guessed_letters = []
    secret_word = get_random_word()

    print(f"{Fore.MAGENTA}Welcome to Snowman Meltdown!{Style.RESET_ALL}")
    print("A secret word has been chosen. Try to save the snowman!\n")

    while True:
        guess = input(f"{Fore.BLUE}Guess a letter: {Style.RESET_ALL}").lower()

        if guess in guessed_letters:
            print(f"{Fore.YELLOW}⚠️  Already guessed this letter! Try again.{Style.RESET_ALL}")
            continue
        elif len(guess) != 1 or not guess.isalpha():
            print(f"{Fore.RED}❌ Please enter a single valid letter.{Style.RESET_ALL}")
            continue

        print(f"You guessed: {Fore.GREEN}{guess}{Style.RESET_ALL}")

        if guess in secret_word:
            guessed_letters.append(guess)
            if all(letter in guessed_letters for letter in secret_word):
                print(f"\n{Fore.GREEN}🎉 Congratulations, you guessed the secret word!{Style.RESET_ALL}")
                print(f"{Fore.CYAN}☃️  The snowman is safe!{Style.RESET_ALL}")
                break
            else:
                print(f"{Fore.GREEN}✅ Correct guess!{Style.RESET_ALL}")
                display_game_stage(mistakes, secret_word, guessed_letters)
        else:
            print(f"{Fore.RED}❌ Wrong guess!{Style.RESET_ALL}")
            mistakes += 1
            display_game_stage(mistakes, secret_word, guessed_letters)
            if mistakes == 3:
                print(f"\n{Fore.RED}💀 Oh no! The snowman melted.{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}📖 The secret word was: {secret_word}{Style.RESET_ALL}")
                break


if __name__ == "__main__":
    while True:
        play_game()
        again = input(f"\n{Fore.MAGENTA}🔁 Play again? (y/n): {Style.RESET_ALL}").strip().lower()
        if again != "y":
            print(f"{Fore.CYAN}👋 Thanks for playing! Goodbye!{Style.RESET_ALL}")
            break