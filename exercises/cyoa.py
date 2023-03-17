"""EX06 - Choose Your Own Adventure - Using functions and procedure to create my own adventure."""

__author__ = "730569503"

points: int = None
player: str = None
plant_name: str = None

def main()-> None:
    global points
    points = 0

    greet()
    print("You can now choose between three different paths. Type 1 to name and water your plant. Type 2 to pick a spot f")
    name_plant()

def greet()-> None:
    global player
    player = input("Welcome to PlantCute, where you will be taking care of a virtual plant. If you take care of your plant well, you will earn points. If you make bad decisions for your plant, you will lose points. What is your name? ")

def name_plant()-> None:
    global plant_name
    global player
    global points
    print(f"Hi, {player}! Let's go ahead and randomly pick out a cute name for your plant.")
    int_input= int(input("Pick a number between 1 and 5, not including 1 and 5. "))
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
    
    print(f"{player}, your plant's name is {plant_name}. Great job naming your plant! You earned 5 points.")
    points += 5

    print(f"Now let's take care of {plant_name} by watering her.")
    water_choice = int(input(f"Type 1 to water {plant_name} with warm water. Type 2 to water {plant_name} with tap water. Type 3 to water {plant_name}  with salt water. "))
    if water_choice < 1 or water_choice > 3:
        water_choice = int(input("Try again! Type 1 to choose warm water. Type 2 to choose tap water. Type 3 to choose salt water."))

    if water_choice == 1:
        print(f"You chose to water {plant_name} with warm water! Great choice, warm water absorbs into soil the best. You earned 15 points.")
        points += 15
    if water_choice == 2:
        print(f"You chose to water {plant_name} with tap water. Good choice, tap water has minerals in it which will enrich your plant. You earned 10 points.")
        points += 10
    if water_choice == 3:
        print(f"You chose to water {plant_name} with salt water. Bad choice, salt water causes deficiences in plants. You lost 5 points.")
        points -= 5

    print(f"{player}, your total number of points is {points}.")

def pick_a_spot(point_value: int) -> int:

    

if __name__ == "__main__":
    main()