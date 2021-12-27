from enum import Enum


class Status(Enum):
    safe = "Safe"
    infected = "Infected"

class Movement(Enum):
    L = "L"
    R = "R"
    F = "F"

class Cell(Enum):
    safe = "O"
    infected = "X"

class Output(Enum):
    INVALID_INPUT = "INVALID INPUT. Refer # INPUT section in Documentation.txt."
    INVALID_DIRECTION = "The direction should be either of N/S/W/E only."
    INVALID_NAVIGATION = "The navigations should exist and should consist of F/R/L only."
    NEGATIVE_INPUT = "The value(s) should be greated than 0."
    UNBOUNDED_COORDINATES = "The coordinates do not lie in the the town."
    INVALID_MOVEMENT = "Invalid path."
