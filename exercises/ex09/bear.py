"""File to define Bear class."""

__author__ = "730569503"


class Bear:
    """Creating a class for Bear."""
    
    age: int
    hunger_score: int

    def __init__(self):
        """Each bear is assigned an age and hunger_score."""
        self.age: int = 0
        self.hunger_score: int = 0
        return None
    
    def one_day(self):
        """Increases age and hunger_score for each bear."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """Updates hunger score when a bear eats fish."""
        self.hunger_score += num_fish
        return None