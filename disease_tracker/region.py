from disease_tracker.constants import Cell, Output, Status
from disease_tracker.person import Person
 

class Region:
    def __call__(self, length: int, breadth: int) -> None:
        self.length : int = length
        self.breadth : int = breadth
        self.__region = [[Cell.safe.value for _ in range(self.breadth)] for _ in range(self.length)]
    
    def set_infected_town(self, x : int, y: int) -> None:
        if x > self.length or x < 0 or y < 0 or y > self.breadth:
            return Output.INVALID_INPUT.value
        self.__region[x][y] = Cell.infected.value

    def walk_through(self, person : Person):
        path = person.movement
        i,j = int(person.initialPosition[0]), int(person.initialPosition[1])
        index = 0
        current_direction = person.initialPosition[2]
        while index < len(path):
            if path[index] != "F":
                current_direction = Region.__set_current_direction(path[index], current_direction)
            else:
                if current_direction == "N": j += 1
                elif current_direction == "S": j -= 1
                elif current_direction == "E": i -= 1
                else : i += 1
                if i > 0 and j > 0 and i < self.length and j < self.breadth:     
                    if self.__region[i][j] != Cell.infected.value:
                        if person.status == Status.infected.value:
                            self.__region[i][j] = Cell.infected.value
                    else:
                        if person.status == Status.safe.value:
                            person.status = Status.infected.value
                else:
                    return Output.INVALID_MOVEMENT.value
            index += 1

    @classmethod
    def __set_current_direction(cls, value : str, current_direction):      
        if value == "R":
            if current_direction == "N":
                return "W"
            if current_direction == "W":
                return "S"
            if current_direction == "S":
                return "E"
            return "N"
        else:
            if current_direction == "N":
                return "E"
            if current_direction == "E":
                return "S"
            if current_direction == "S":
                return "W"
            return "N"

    def display_virus_propagation(self):
        n = len(self.__region[0])
        for i in range(n):
            for j in range(n):
                if i > j:
                    self.__region[i][j],self.__region[j][i] = self.__region[j][i],self.__region[i][j]
        i,j = 0, n-1
        while i < j:
            for k in range(n):
                self.__region[i][k],self.__region[j][k] = self.__region[j][k],self.__region[i][k]
            i += 1
            j -= 1

        for i in range(self.length):
            print("".join(self.__region[i]))

        i,j = 0, n-1
        while i < j:
            for k in range(n):
                self.__region[i][k],self.__region[j][k] = self.__region[j][k],self.__region[i][k]
            i += 1
            j -= 1
        for i in range(n):
            for j in range(n):
                if i < j:
                    self.__region[i][j],self.__region[j][i] = self.__region[j][i],self.__region[i][j]

    def __str__(self) -> str:
        return f"length : {self.length}, breadth : {self.breadth}, `\n region : {self.__region}"

    