"""EX02 - One-shot Wordle - You have one shot to guess the secret word!"""

__author__: str = "730569503"

secret = "python"
secret_len = str(len(secret))
guess = input(f"What is your {secret_len}-letter guess? ")  # player input

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

index: int = 0 
emoji_result: str = ""
check_indice: int = 0
guess_indice: bool = False

while len(guess) != len(secret):  # if guess isn't the correct length, have the player try again
    guess = input(f"That was not {secret_len} letters! Try again: ")

while index < len(guess):
    if guess[index] == secret[index]:
        emoji_result = emoji_result + GREEN_BOX  # print a green box if character correctly matches with index
    else:
        guess_indice = False
        while guess_indice is False and check_indice < len(secret):
            if guess[index] == secret[check_indice]:
                guess_indice = True  # if character is present elsewhere, print a yellow box
            check_indice = check_indice + 1
        if guess_indice is True:
            emoji_result = emoji_result + YELLOW_BOX
        else:
            emoji_result = emoji_result + WHITE_BOX  # if character is not present anywhere, print a white box
    index = index + 1
    check_indice = 0
    
print(emoji_result)

if guess == secret:  # correct guess
    print("Woo! You got it!")
else:  # incorrect guess
    print("Not quite. Play again soon!") 