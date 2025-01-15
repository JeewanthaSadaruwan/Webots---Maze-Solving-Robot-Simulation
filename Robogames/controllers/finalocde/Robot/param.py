
from controller import Robot

# Initialize the robot and timestep
robot = Robot()
timestep = int(robot.getBasicTimeStep())


#Define speed
SPEED = 2.0
THRESHOLD = 2500

wheelRadius = 0.0205
wheelCircumference = 2.0 * 3.141592 * wheelRadius
wheelBase = 0.052

#parameters of buzzer
# Parameters for the sound
calibration_sound = "calibration.wav"      # Sound file name
volume = 1.0           # Full volume
pitch = 1.0           # Normal pitch
balance = 0.0         # Centered balance
loop = False          # Don't loop the sound


#PD control
previous_error = 0.0
forward_kp = 0.01
forward_kd = 0.05