"""EX06 - Choose Your Own Adventure - Using functions and procedure to create my own adventure."""

__author__ = "730569503"

points: int = None
player: str = None
plant_name: str = "your plant"


def main()-> None:
    global points
    points = 0
    game_ending: bool = False

    greet()

    while game_ending == False:
        path_choice: int = int(input(f"{player}, you can choose between three different paths. Type 1 to name and water your plant. Type 2 to pick a spot for your plant. Type 3 to end your experience. "))
        if path_choice < 1 or path_choice > 3:
            path_choice: int = int(input("Try again! Type either 1, 2, or 3 to choose a path."))
        elif path_choice == 1:
            name_and_water_plant()
            print(f"You have a total of {points} points.")
        elif path_choice == 2:
            pick_a_spot_return: int = pick_a_spot(points)
            points = pick_a_spot_return
            print(f"You have a total of {points} points.")
        if path_choice == 3:
            end()
            game_ending = True

    
def greet()-> None:
    global player
    player = input("Welcome to PlantCute, where you will be taking care of a plant. If you take care of your plant well, you will earn points. If you make bad decisions for your plant, you will lose points. What is your name? ")


def name_and_water_plant()-> None:
    global plant_name
    global player
    global points
    print(f"Hi, {player}! Let's go ahead and randomly pick out a cute name for your plant.")
    int_input: int = int(input("Pick a number between 1 and 5, not including 1 and 5. "))
    if int_input <= 1 or int_input >= 5:
        int_input = input(f"{player}, your chosen number was out of range. Try again!")
    import random
    random_integer: int = random.randint(1,2)
    int_input_with_randint: int = random_integer + int_input
    if int_input_with_randint == 3:
        plant_name = "Mochi"
    if int_input_with_randint == 4:
        plant_name = "Peach"
    if int_input_with_randint == 5:
        plant_name = "Ginny"
    if int_input_with_randint == 6:
        plant_name = "Melody"
    
    print(f"{player}, your plant's name is {plant_name}. Great job naming your plant! You earned 10 points.")
    points += 10

    print(f"Now let's take care of {plant_name} by watering her.")
    water_choice: int = int(input(f"Type 1 to water {plant_name} with warm water. Type 2 to water {plant_name} with tap water. Type 3 to water {plant_name}  with salt water. "))
    if water_choice < 1 or water_choice > 3:
        water_choice = int(input("Try again! Type 1 to choose warm water. Type 2 to choose tap water. Type 3 to choose salt water."))

    if water_choice == 1:
        print(f"You chose to water {plant_name} with warm water! Great choice, warm water absorbs into soil the best. You earned 15 points.")
        points += 15
    elif water_choice == 2:
        print(f"You chose to water {plant_name} with tap water. Good choice, tap water has minerals in it which will enrich your plant. You earned 10 points.")
        points += 10
    else:
        print(f"You chose to water {plant_name} with salt water. Bad choice, salt water causes deficiences in plants. You lost 5 points.")
        points -= 5


def pick_a_spot(point_value: int) -> int:
    global plant_name
    global player

    spot_choice: int = int(input(f"{player}, it's time to pick a spot for {plant_name}. Type 1 to place your plant in the backyard. Type 2 to place your plant under a LED light. Type 3 to place your plant in the basement."))
    if spot_choice < 1 or spot_choice > 3:
        spot_choice: int = int(input("Try again! Type 1 to place your plant in the backyard. Type 2 to place your plant under a LED light. Type 3 to put your place in the basement."))

    if spot_choice == 1:
        print(f"Great job, {player}! Your backyard is a great place for {plant_name} because it is outdoors and ensures that your plant receives sunlight. You earned 15 points.")
        point_value += 15
    elif spot_choice == 2:
        print(f"Not bad, {player}! While placing {plant_name} outdoors is the most ideal, LED lights are the most efficient way to grow a plant indoors. You earned 10 points.")
        point_value += 10
    else:
        print(f"Bad choice, {player}. The basement provides no oppurtunity for {plant_name} to receive sunlight. You lost 5 points.")
        point_value -= 5

    return point_value


def end()-> None:
    global points
    global plant_name
    print(f"Thank you for playing PlantCute! You took great care of {plant_name}. You earned {points} points total.")


if __name__ == "__main__":
    main()