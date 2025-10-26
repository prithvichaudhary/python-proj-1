import random

easy_words = ['cat', 'dog', 'fish', 'bird', 'tree']
medium_words = ['python', 'jumble', 'garden', 'window', 'bottle']
hard_words = ['xylophone', 'quizzical', 'juxtapose', 'mnemonic', 'zephyr']
def get_random_word(difficulty):
    if difficulty == 'easy':
        return random.choice(easy_words)
    elif difficulty == 'medium':
        return random.choice(medium_words)
    elif difficulty == 'hard':
        return random.choice(hard_words)
    else:
        raise ValueError("Invalid difficulty level. Choose from 'easy', 'medium', or 'hard'.") 
def scramble_word(word):
    word = list(word)
    random.shuffle(word)
    return ''.join(word)
def main():
    print("Welcome to the Guess the Random Word Game!")
    difficulty = input("Choose a difficulty level (easy, medium, hard): ").lower()
    try:
        word_to_guess = get_random_word(difficulty)
    except ValueError as e:
        print(e)
        return
    scrambled = scramble_word(word_to_guess)
    print(f"Scrambled word: {scrambled}")
    attempts = 3
    while attempts > 0:
        guess = input("Your guess: ").strip().lower()
        if guess == word_to_guess:
            print("Congratulations! You guessed the word correctly.")
            return
        else:
            attempts -= 1
            print(f"Incorrect! You have {attempts} attempts left.")
    print(f"Sorry, you've run out of attempts. The correct word was '{word_to_guess}'.")
if __name__ == "__main__":
    main()