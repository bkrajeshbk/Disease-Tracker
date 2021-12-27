from disease_tracker.constants import Status
from typing import List


class Person:
    def __init__(self) -> None:
        pass

    def __call__(self, details: List) -> None:
        self.initialPosition = details[0]
        self.movement = details[1]
        self.status = Status.safe.value

    def __str__(self) -> str:
        return f"Position : {self.initialPosition}, Path : {self.movement}, Status : {self.status}"


