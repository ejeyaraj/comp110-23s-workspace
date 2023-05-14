"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730569503"


class Simpy:
    """A utility class for numerical operations."""

    values: list[float]

    def __init__(self, values: list[float]):
        """Will initialize a new Simpy object."""
        self.values = values

    def __str__(self) -> str:
        """Will return a string representation of the Simpy object."""
        return f"Simpy({self.values})"

    def fill(self, value: float, num_values: int) -> None:
        """Will fill the Simpy object with a given numerical value a specified number of times."""
        self.values = [value] * num_values

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Will fill the Simpy object with a sequence of numerical values starting from a specified start point and ending at a specified stop point."""
        assert step != 0.0
        self.values = []
        val = start
        while (step > 0 and val < stop) or (step < 0 and val > stop):
            self.values.append(val)
            val += step

    def sum(self) -> float:
        """Will compute and returns the sum of the values in the Simpy object."""
        return sum(self.values)
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Will add a numerical value or another Simpy object to the Simpy object."""
        result_values: list[Union[float, Simpy]] = []
        if isinstance(rhs, float):
            for item in self.values:
                result_values.append(item + rhs)
            return Simpy(result_values)
        elif isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result_values.append(self.values[i] + rhs.values[i])
            return Simpy(result_values)

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Will raise the values in the Simpy object to a given power."""
        result_values: list[Union[float, Simpy]] = []
        if isinstance(rhs, float):
            for item in self.values:
                result_values.append(item ** rhs)
            return Simpy(result_values)
        elif isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result_values.append(self.values[i] ** rhs.values[i])
            return Simpy(result_values)

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Will compare the values in the Simpy object with a given numerical value or another Simpy object for equality."""
        result_values: list[Union[float, Simpy]] = []
        if isinstance(rhs, float):
            for item in self.values:
                result_values.append(item == rhs)
            return result_values
        elif isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result_values.append(self.values[i] == rhs.values[i])
            return result_values
        
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Will compare the values in the Simpy object with a given numerical value or another Simpy object for greater than."""
        result_values: list[Union[float, Simpy]] = []
        if isinstance(rhs, float):
            for item in self.values:
                result_values.append(item > rhs)
            return result_values
        elif isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result_values.append(self.values[i] > rhs.values[i])
            return result_values

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Will return either a single value or a Simpy object containing selected values."""
        result_values: list[Union[float, Simpy]] = []
        if isinstance(rhs, int):
            return self.values[rhs]
        elif isinstance(rhs, list):
            assert len(rhs) == len(self.values)
            for i in range(len(rhs)):
                if rhs[i]:
                    result_values.append(self.values[i])
            return Simpy(result_values)