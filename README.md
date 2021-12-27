# Information :
This project is implement in python and showcases OOPS concept namely abstraction, encapsulation, inheritance and exception handling. 
The project is provided with a sample test_pack file which covers all the scenarios/edgecases.

# Direction of Use:
- python -m disease_tracker_code <absolute_path_to_filename>. Please refer #INPUT section for more details.

# NOTE: 
Use "py" in place of "python" in above commands for venv 3.10.

# PROBLEM:
The Center for Disease Control and Prevention is trying to model disease propagation for a particular virus. The virus is known to transmit through human contact and the study aims to simulate how various towns in a region can get infected by the movement of people. The scientists have come up with the following simple model for this scenario:

The whole region is defined as a rectangular region with dimensions LxH, with each cell representing a single town. 

To begin with, only a small number of towns are infected by the virus. The virus is known to spread when a person moves from any infected town to an adjacent town.

The initial list of infected towns is provided as a list of x and y coordinates. For example, a value of <0, 0> would indicate the bottom-left corner cell in the region is an infected town.

A person's location is represented by x and y coordinates. Their heading is represented by one of four cardinal compass points. An example position could be <0, 0, N>, which means that the person is at the bottom-left corner and facing up. 

As a person moves through the region, if they happen to move through a cell which is infected, every subsequent cell they enter will end up being infected. 

A person's movements through the region is represented by a limited set of operations: 

L -- makes the person turn left 90 degrees
R -- makes the person turn right 90 degrees
F -- makes the person move forward 1 square

Assume the square directly north of <x, y> is <x, y+1>.

# INPUT:
The first line of input represents the size of the region specifically length and breadth separated by a single space. The base index being <0, 0>.
The second line contains a number N, indicating the initial count of infected towns
This is followed by N lines, where each line represents the location of a single infected town. This is provided as an x and y coordinates separated by a single space.
The rest of the input is data pertaining to the movement of various persons. Each single person has two lines of input. The first line gives the person's position and heading all three separated by a single space. The second line is the sequence of operations that show where the person navigated.
Each person will finish their navigation sequentially, which means that the second person won't start moving until the first one has finished moving.
# NOTE: The test file should have 2 empty lines at the end to be processed completely.

# OUTPUT:
The output should be a region of characters denoting the infection state of the region after all persons have completed their movements.
O = no infection
X = infected

# SAMPLE INPUT AND OUTPUT:
Input:
{
  "region": {"length": 5, "breadth":  5},
  "infectedCells": [{"x":  1, "y":  1}, {"x":  2, "y":  3}],
  "persons": [
    {"initialPosition": "1 0 N", "movement:" "FFRFFRF"},
    {"initialPosition": "1 3 S", "movement": "LFFLFRFRFF"}
  ]
}
Expected output:

OOOXX
OOXXX
OXXXX
OXOXO
OOOOO
--====--