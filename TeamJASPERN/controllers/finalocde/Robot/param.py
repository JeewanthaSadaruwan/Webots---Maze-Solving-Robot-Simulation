
from controller import Robot

# Initialize the robot and timestep
robot = Robot()
timestep = int(robot.getBasicTimeStep())

# supervisor = Supervisor()
# robot_node = supervisor.getFromDef("epuck")
# # Set translation field (x, y, z coordinates)
# initial_translation = [1.0, 0, 1.0]  # x=1, y=0, z=1
# robot_node.getField("translation").setSFVec3f(initial_translation)

#Define speed
forward_SPEED = 5.0
turning_SPEED = 2.0
THRESHOLD = 2500

wheelRadius = 0.0205
wheelCircumference = 2.0 * 3.141592 * wheelRadius
wheelBase = 0.052

#parameters of buzzer
# Parameters for the sound
calibration_sound = "calibration.wav"      # Sound file name
music = "mingle.wav"
end = "end.wav"
volume = 1.0           # Full volume
pitch = 1.0           # Normal pitch
balance = 0.0         # Centered balance
# loop = True          # Don't loop the sound



#PD control
previous_error = 0.0
forward_kp = 0.01
forward_kd = 0.05

#sensor detection threasholds
leftTH = 2500
rightTH = 2500
frontlTH = 2500
frontrTH = 2500

# def initialize_maze(rows, cols):
#     maze = [[0 for _ in range(cols)] for _ in range(rows)]
#     flood_values = [[float('inf') for _ in range(cols)] for _ in range(rows)]
#     return maze, flood_values

# maze, flood_values = initialize_maze(10, 10)
# goal = (7, 7)
# position = (8, 9)
# orientation = 1  # 0: up, 1: down, 2: left, 3: right


# Wall direction constants
NORTH = 1
EAST = 2
SOUTH = 4
WEST = 8


maze = [
    [11, 9, 5, 5, 5, 5, 3, 9, 5, 3],
    [8, 6, 9, 3, 9, 5, 2, 10, 9, 6],
    [10, 11, 10, 12, 6, 13, 4, 6, 8, 7],
    [10, 12, 2, 9, 3, 9, 5, 3, 8, 3],
    [10, 9, 2, 10, 12, 6, 9, 2, 10, 10],
    [10, 10, 14, 10, 9, 5, 6, 8, 6, 14],
    [14, 10, 9, 6, 12, 7, 11, 12, 5, 3],
    [9, 6, 12, 5, 5, 3, 12, 5, 1, 6],
    [12, 3, 9, 3, 11, 10, 9, 3, 10, 11],
    [13, 4, 6, 12, 6, 14, 14, 12, 4, 6]
]

current_x = 9
current_y = 8
direction = SOUTH

current_dir = 'S'  # Assuming starting direction is south

