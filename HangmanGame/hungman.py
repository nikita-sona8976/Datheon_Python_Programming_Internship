import random

# ASCII Art stages for the gallows (0 to 6 incorrect guesses)
HANGMAN_STAGES = [
    """
       ------
       |    |
            |
            |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
            |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
       |    |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
      /|    |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
      /|\\   |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
      /|\\   |
      /     |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
      /|\\   |
      / \\   |
            |
    =========
    """
]

# Word list for the game
WORD_LIST = [
    "python", "developer", "programming", "hangman", 
    "computer", "algorithm", "variable", "function", "syntax"
]

def play_hangman():
    word = random.choice(WORD_LIST).lower()
    word_letters = set(word)
    guessed_letters = set()
    
    incorrect_guesses = 0
    max_incorrect = 6

    print("========================================")
    print("      WELCOME TO CONSOLE HANGMAN!       ")
    print("========================================")

    while incorrect_guesses < max_incorrect and len(word_letters) > 0:
        print(HANGMAN_STAGES[incorrect_guesses])
        
        word_display = [letter if letter in guessed_letters else '_' for letter in word]
        print("Word to guess: " + " ".join(word_display))
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        print(f"Remaining attempts: {max_incorrect - incorrect_guesses}")
        
        user_guess = input("\nGuess a letter: ").lower().strip()
        
        if not user_guess.isalpha() or len(user_guess) != 1:
            print("❌ Invalid input. Please enter a single alphabetical letter.")
            continue
            
        if user_guess in guessed_letters:
            print(f"⚠️ You already guessed the letter '{user_guess}'. Try a different one!")
            continue
            
        guessed_letters.add(user_guess)
        
        if user_guess in word_letters:
            word_letters.remove(user_guess)
            print(f"✅ Good job! '{user_guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"❌ Sorry, '{user_guess}' is not in the word.")
            
        print("-" * 40)

    if len(word_letters) == 0:
        print("\n🎉 CONGRATULATIONS! YOU WON! 🎉")
        print(f"The word was: {word.upper()}")
    else:
        print(HANGMAN_STAGES[max_incorrect])
        print("\n💀 GAME OVER! YOU LOST! 💀")
        print(f"The correct word was: {word.upper()}")

if __name__ == "__main__":
    play_hangman()