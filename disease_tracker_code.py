import sys
from disease_tracker.constants import Output 
from disease_tracker.region import Region
from disease_tracker.person import Person


class DiseaseTracker():
    def __init__(self) -> None:
        self.length : int = None
        self.breadth : int = None
        self.infected_count : int = 0
        self.infected_index : list = []
        self.people : list = []
        self.position : str = ""
        self.movement : str = ""

    def get_details(self, instruction):
        instruction_index = 0
        try:
            dimensions = instruction[instruction_index]
            instruction_index += 1
            if str(dimensions) != None:
                self.length,self.breadth = dimensions.split(" ")
                self.length = int(self.length)
                self.breadth = int(self.breadth)
                if self.length <= 0 or self.breadth <= 0:
                    raise Exception(Output.NEGATIVE_INPUT.value)
        except ValueError:
            raise ValueError(f"Region's area : {Output.INVALID_INPUT.value}")
        try:
            self.infected_count = int(instruction[instruction_index])
            instruction_index += 1
            if self.infected_count <= 0:
                raise Exception(Output.NEGATIVE_INPUT.value)
        except ValueError: 
            raise ValueError(f"Infected Count Details : {Output.INVALID_INPUT.value}")
        try:
            self.infected_index = []
            for _ in range(int(self.infected_count)):
                coordinates = instruction[instruction_index]
                if str(coordinates) != None:
                    x_coordinate, y_coordinate = coordinates.split(" ")
                    x_coordinate = int(x_coordinate)
                    y_coordinate = int(y_coordinate)
                    if x_coordinate < 0 or y_coordinate < 0:
                        raise Exception(Output.NEGATIVE_INPUT.value)
                    self.infected_index.append([x_coordinate, y_coordinate])
                instruction_index += 1
        except ValueError: 
            raise ValueError(f"Infected town details : {Output.INVALID_INPUT.value}")
        try:
            self.people = []
            self.position = instruction[instruction_index]
            while self.position != "\n":
                instruction_index += 1
                x_position, y_position, direction = self.position.split(" ")
                x_position = int(x_position)
                y_position = int(y_position)
                direction = str(direction)
                if x_position < 0 or y_position < 0:
                    raise Exception(Output.NEGATIVE_INPUT.value)
                if x_position > self.length or y_position > self.breadth:
                    raise Exception(Output.UNBOUNDED_COORDINATES.value)  
                if not (direction == "N" or direction == "S" or direction == "E" or direction == "W"):
                    raise Exception(Output.INVALID_DIRECTION.value)
                movement = str(instruction[instruction_index])
                instruction_index += 1
                for ch in movement:
                    if ch != "F" and ch != "L" and ch != "R":
                        raise Exception(Output.INVALID_NAVIGATION.value)
                self.people.append([[x_position, y_position, direction], movement])
                self.position = instruction[instruction_index]
        except ValueError: 
            raise ValueError(f"Person(s) details : {Output.INVALID_INPUT.value}")
        if self.people == []:
            region = Region()
            region(self.length,self.breadth)
            print("No traveller to spread the Virus.\nOutput :\n")
            region.display_virus_propagation()
            return 1

    def execute(self):
        region = Region()
        region(self.length,self.breadth)
        if self.infected_count == 0:
            region.display_virus_propagation()
            print("Exiting as there are no infected towns in the region.")
            return
        for x_coordinate, y_coordinate in self.infected_index:
            region.set_infected_town(x_coordinate, y_coordinate)
        #print("Region's Initial Virus Propagation Status:\n")
        #region.display_virus_propagation()
        for details in self.people:
            person = Person()
            person(details)
            #print("\nPerson", person)
            region.walk_through(person)
        #print("Region's Final Virus Propagation Status:\n")
        region.display_virus_propagation()

    def translate(self, filename : str = "./sample_test_pack.txt"):
        print(f"Given File : {filename}")
        disease_details = []
        with open(filename, 'r') as fr:
            line = fr.readline()
            detail = []
            while line:
                if line == "\n":
                    detail.append("\n")
                    disease_details.append(detail)
                    detail = []
                else:
                    detail.append(line.replace("\n",""))
                line = fr.readline()
        print("Instructions : \n",disease_details)
        if not disease_details:
            raise Exception(f"No details given to proceed. Exiting...: {Output.INVALID_INPUT.value}")
        print(f"No of details : {len(disease_details)}")
        i = 0
        for detail in disease_details:
            i += 1
            try :
                print(f"\nTC = #{i} \nRegion detials : {detail}\n")
                if self.get_details(detail) == 1:
                    continue
                print("Output : \n")
                self.execute()
            except Exception as e:
                print(e)
                continue

def main():
    diseaseTracker = DiseaseTracker()
    try:
        if len(sys.argv) > 1:
            filename = sys.argv[1]
            diseaseTracker.translate(filename)
        else:
            diseaseTracker.translate()
    except Exception as e:
        print(e)
        return

if __name__ == "__main__":
    main()