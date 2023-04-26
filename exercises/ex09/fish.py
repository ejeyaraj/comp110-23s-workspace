"""File to define Fish class."""

__author__ = "730569503"


class Fish:
    """Creating a class for Fish."""
    
    age: int

    def __init__(self):
        """Assigns each fish an age."""
        self.age: int = 0
        return None
    
    def one_day(self):
        """Increases the age of fish."""
        self.age += 1
        return None