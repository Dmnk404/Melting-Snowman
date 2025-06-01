from game_logic import play_game

if __name__ == "__main__":
    while True:
        play_game()
        again = input("\n🔁 Play again? (y/n): ").strip().lower()
        if again != "y":
            print("👋 Thanks for playing! Goodbye!")
            break