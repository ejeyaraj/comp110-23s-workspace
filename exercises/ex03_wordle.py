"""EX03 - Structured Wordle - You have six shots to guess the secret word!"""

__author__: str = "730569503"


def contains_char(word: str, character: str) -> bool:
    """The function returns true if a given character if present in a word, and
    returns false if the character is not present in the word."""

    assert len(character) == 1
    check_indice: int = 0
    guess_indice: bool = False
    
    while guess_indice is False and check_indice < len(word):
        if word[check_indice] == character: 
            guess_indice = True
        check_indice = check_indice + 1
    if guess_indice is True:
        return True  # character is present in a word, and function returns true
    else:
        return False  # character is not present in a word, and function returns false

def emojified(guess: str, secret_word: str) -> str:
    """The function, given the input of two string with equal length, outputs emoji boxes
    that represent whether the character matched a specific indice. It uses the contains_char function
    to test for the yellow or white box output."""

    GREEN_BOX: str = "\U0001F7E9"
    WHITE_BOX: str = "\U00002B1C"
    YELLOW_BOX: str = "\U0001F7E8"
    emoji_result = ""

    index = 0
    assert len(guess) == len(secret_word)

    while index < len(guess):
        if guess[index] == secret_word[index]:  # prints green box since a character matches exactly with a character in the secret word
            index = index + 1
            emoji_result = emoji_result + GREEN_BOX
        else:
            if(contains_char(secret_word, guess[index])) == True:  # call the contains_char function, and the function returns true(character is present in the secret word) so a yellow box is printed
                index = index + 1
                emoji_result = emoji_result + YELLOW_BOX
            else:  # contains_char returns false(character is not present in the secret word), so a white box is printed
                index = index + 1
                emoji_result = emoji_result + WHITE_BOX
    return emoji_result  # prints full string of boxes

def input_guess(length_input: int) -> str:
    word_input = input(f"Enter a {length_input} character word: ")

    while length_input != len(word_input):  # the guess isn't the correct length, so the player has to try again
        word_input = input(f"That wasn't {length_input} chars! Try again: ")
        
    if length_input == len(word_input):  # the guess is the correct length, so return the guess word
            return word_input

    return word_input

def main() -> None:
    """The entrypoint of the program and the main game loop."""
    secret_word = "apple"
    user_turns: int = 1
    game_outcome: bool = False
    max_turns: int = 6

    while user_turns < max_turns + 1 and game_outcome == False:
        print(f"=== Turn {user_turns}/{max_turns} ===")
        guess_input = input_guess(len(secret_word))  # assigns variable to the the guess word input
        print(emojified(guess_input, secret_word))  # calls emojified to return string of boxes
        if guess_input == secret_word:  # the guess is correct,  and the game ends 
            game_outcome = True
        else:
            user_turns = user_turns + 1  # the guess is incorrect, so the user gets another turn

    N: int = user_turns
    if game_outcome == True:
        print(f"You won in {N}/{max_turns} turns!")
    
    if user_turns >= max_turns + 1:
        print(f"X/{max_turns} - Sorry, try again tomorrow!")

if __name__ == "___main__":
    main()

main()




