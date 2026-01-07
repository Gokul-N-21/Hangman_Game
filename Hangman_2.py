import random

def load_words():
    words_list = []
    # 'r' means "read" mode
    with open('Hangman_Words.txt', 'r') as f:
        for line in f:
            # .strip() removes the "Enter" key (\n) from the end of the word
            # .upper() makes sure the word is in all caps
            word = line.strip().upper()
            
            # Only add the word if it's not an empty line
            if word:
                words_list.append(word)
    
    return words_list

STAGES = [
    # Final stage: head, torso, both arms, and both legs
    """
       --------
       |      |
       |      O
       |     \\|/
       |      |
       |     / \\
       -
    """,
    # Head, torso, both arms, and one leg
    """
       --------
       |      |
       |      O
       |     \\|/
       |      |
       |     / 
       -
    """,
    # Head, torso, and both arms
    """
       --------
       |      |
       |      O
       |     \\|/
       |      |
       |      
       -
    """,
    # Head, torso, and one arm
    """
       --------
       |      |
       |      O
       |     \\|
       |      |
       |      
       -
    """,
    # Head and torso
    """
       --------
       |      |
       |      O
       |      |
       |      |
       |      
       -
    """,
    # Head
    """
       --------
       |      |
       |      O
       |    
       |      
       |      
       -
    """,
    # Empty gallows
    """
       --------
       |      |
       |      
       |    
       |      
       |      
       -
    """
]

def choose_word(words):
    word = random.choice(words)
    return word

def get_guess(guessed_letters):
    while True:
        guess = input("Guess a letter: ").upper()
        
        if len(guess) != 1:
            print("Please enter only ONE letter.")
        elif not guess.isalpha():
            print("Please enter a valid alphabet letter (A-Z).")
        elif guess in guessed_letters:
            print("You already guessed that letter! Try a different one.")
        else:
            return guess # Return just the letter

def get_display(word, guessed_letters):
    display_str = ""
    for letter in word:
        if letter in guessed_letters:
            display_str += letter + " "
        else:
            display_str += "_ "
    return display_str

def run_game():
    words = load_words()
    secret_word = choose_word(words)
    lives = 6
    guessed_letters = []

    print("Welcome to Hangman!!")

    while True:
        # 1. Always get the current display string at the start
        current_display = get_display(secret_word, guessed_letters)
        
        # 2. Show the visuals
        print(STAGES[lives]) # This prints the gallows based on lives
        print(f"Word: {current_display}")
        print(f"Lives left: {lives}")
        print(f"Guessed so far: {', '.join(guessed_letters)}")

        # 3. Get the guess
        guess = get_guess(guessed_letters)
        guessed_letters.append(guess)

        # 4. Check the guess
        if guess in secret_word:
            print(f"\nYes! '{guess}' is in the word! 🎉")
            # We need to update the display again to check for a win
            if '_ ' not in get_display(secret_word, guessed_letters):
                print(f"Congratulations! The word was: {secret_word}")
                break
        else:
            print(f"\nOops! '{guess}' is not there. ❌")
            lives -= 1
            if lives == 0:
                print(STAGES[0]) # Show the final hangman
                print(f"GAME OVER! The word was: {secret_word}")
                break

if __name__ == "__main__":
    run_game()
