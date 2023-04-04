"""EX06 - Choose Your Own Adventure - Using functions and procedure to create my own adventure, PlantGames."""
import random

__author__ = "730569503"

points: int
player: str
plant_name: str = "your plant"
plant_emoji: str = "\U0001FAB4"
water_emoji: str = "\U0001F4A7"
katniss_emoji: str = "\U0001F3F9"
primrose_emoji: str = "\U0001F339"
peeta_emoji: str = "\U0001F3A8"
gale_emoji: str = "\U0001FAA8"


def main() -> None:
    """This function returns none, initializes the global variable points, and runs the main game loop by calling functions."""
    global points
    global player
    points = 0
    game_ending: bool = False

    greet()

    while game_ending is False:
        path_choice: int = int(input(f"{player}, you can choose between three different paths. Type 1 to name and water your plant. Type 2 to pick a spot for your plant to grow. Type 3 to say goodbye and end your experience. "))
        if path_choice < 1 or path_choice > 3:
            path_choice = int(input(f"Try again, {player}! Type either 1, 2, or 3 to choose a path."))
        elif path_choice == 1:
            name_and_water_plant()
            print(f"{player}, you have a total of {points} points.")
        elif path_choice == 2:
            pick_a_spot_return: int = pick_a_spot(points)
            points = pick_a_spot_return
            print(f"{player}, you have a total of {points} points.")
        else:
            end()
            game_ending = True

    
def greet() -> None:
    """This procedure greets the player, gets the input for the player's name, and returns none."""
    global player
    global plant_emoji
    print(f"Welcome to PlantGames{plant_emoji}, where you will be taking care of a plant. If you take care of your plant well, you will earn points. If you make bad decisions for your plant, you will lose points. ")
    player = input("What is your name? ")


def name_and_water_plant() -> None:
    """This procedure helps name the plant randomly and helps water the plant based off of the user's choices."""
    global plant_name
    global player
    global points
    global water_emoji
    global plant_emoji
    global katniss_emoji
    global peeta_emoji
    global primrose_emoji
    global gale_emoji
    print(f"{player}, let's randomly pick a name for your plant{plant_emoji}.")
    int_input: int = int(input(f"{player}, pick a number between 1 and 5, not including 1 and 5. "))
    if int_input <= 1 or int_input >= 5:
        int_input = int(input(f"{player}, your chosen number was out of range. Try again!"))
    random_integer: int = random.randint(1, 2)
    int_input_with_randint: int = random_integer + int_input
    if int_input_with_randint == 3:
        plant_name = f"Katniss{katniss_emoji}"
    elif int_input_with_randint == 4:
        plant_name = f"Primrose{primrose_emoji}"
    elif int_input_with_randint == 5:
        plant_name = f"Gale{gale_emoji}"
    else:
        plant_name = f"Peeta{peeta_emoji}"
    
    print(f"{player}, your plant's name is {plant_name}. Great job naming your plant! You earned 10 points.")
    points += 10

    print(f"{player}, now let's take care of {plant_name} by watering it{water_emoji}.")
    water_choice: int = int(input(f"Type 1 to water {plant_name} with warm water. Type 2 to water {plant_name} with tap water. Type 3 to water {plant_name} with salt water. "))
    if water_choice < 1 or water_choice > 3:
        water_choice = int(input(f"Try again, {player}! Type 1 to choose warm water. Type 2 to choose tap water. Type 3 to choose salt water."))
    elif water_choice == 1:
        print(f"You chose to water {plant_name} with warm water{water_emoji}! Great choice {player}, warm water absorbs into soil the best. You earned 15 points.")
        points += 15
    elif water_choice == 2:
        print(f"You chose to water {plant_name} with tap water{water_emoji}. Good choice {player}, tap water has minerals in it which will enrich your plant. You earned 10 points.")
        points += 10
    else:
        print(f"You chose to water {plant_name} with salt water{water_emoji}. Bad choice {player}, salt water causes deficiences in plants. You lost 5 points.")
        points -= 5


def pick_a_spot(point_value: int) -> int:
    """This function uses a local variable as a parameter to keep track of the points and updates it based off of user choices."""
    global plant_name
    global player
    spot_choice: int = int(input(f"{player}, it's time to pick a spot for {plant_name}. Type 1 to place your plant in the backyard. Type 2 to place your plant under a LED light. Type 3 to place your plant in the basement."))
    if spot_choice < 1 or spot_choice > 3:
        spot_choice = int(input(f"Try again, {player}! Type 1 to place your plant in the backyard. Type 2 to place your plant under a LED light. Type 3 to put your place in the basement."))
    elif spot_choice == 1:
        print(f"Great job, {player}! Your backyard is a great place for {plant_name} because it is outdoors and ensures that your plant receives sunlight. You earned 15 points.")
        point_value += 15
    elif spot_choice == 2:
        print(f"Not bad, {player}! While placing {plant_name} outdoors is the most ideal, LED lights are the most efficient way to grow a plant indoors. You earned 10 points.")
        point_value += 10
    else:
        print(f"Bad choice, {player}. The basement provides no oppurtunity for {plant_name} to receive sunlight. You lost 5 points.")
        point_value -= 5

    return point_value


def end() -> None:
    """This function ends the game with a goodbye message and a message with how many total points were earned."""
    global points
    global plant_name
    global player
    print(f"{player}, thank you for playing PlantGames{plant_emoji}! You took great care of {plant_name}. You earned {points} points total.")


if __name__ == "__main__":
    main()