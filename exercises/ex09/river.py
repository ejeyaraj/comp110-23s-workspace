"""File to define River class."""

__author__ = "730569503"

from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear


class River:
    """Creating a class for River that stimulates the life of bears and fishes."""

    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int) -> None:
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())
        return None

    def check_ages(self) -> None:
        """At a certain age, animals are removed from the river."""
        bears_list: list[Bear] = []
        fish_list: list[Fish] = []
        for elem in self.fish:
            if elem.age <= 3:
                fish_list.append(elem)
        for elem in self.bears:
            if elem.age <= 5:
                bears_list.append(elem)
        self.fish = fish_list
        self.bears = bears_list
        return None

    def bears_eating(self) -> None:
        """If there are at least 5 fish in the river, the bear will eat 3 fish."""
        for i in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                i.eat(3)
        return None        
    
    def check_hunger(self) -> None:
        """Remove starving bears from the bears list."""
        bears_list: list[Bear] = []
        for i in self.bears:
            if i.hunger_score >= 0:
                bears_list.append(i)
        self.bears = bears_list
        return None
        
    def repopulate_fish(self) -> None:
        """Taking into account repoppulation when counting fish."""
        offspring_fish: int = (len(self.fish) // 2) * 4
        for i in range(0, offspring_fish):
            self.fish.append(Fish())
        return None
    
    def repopulate_bears(self) -> None:
        """Taking into account repoppulation when counting bears."""
        offspring_bears: int = (len(self.bears) // 2)
        for i in range(0, offspring_bears):
            self.bears.append(Fish())
        return None
    
    def view_river(self) -> None:
        """Prints river information, like day and number of bears and fish."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None
            
    def one_river_day(self) -> None:
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
        return None

    def one_river_week(self) -> None:
        """Simulate one week of life in the river."""
        for i in range(0, 7):
            self.one_river_day()
        return None
    
    def remove_fish(self, amount: int) -> None:
        """Remove a certain number of fish from the river."""
        for i in range(0, amount):
            self.fish.pop(i)
        return None