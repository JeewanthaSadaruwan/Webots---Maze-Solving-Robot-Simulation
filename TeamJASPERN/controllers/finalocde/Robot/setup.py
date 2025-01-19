from controller import Robot
from controller import Supervisor
from Robot import param
import math

#initialize motors
left_motor = param.robot.getDevice("left wheel motor")
right_motor = param.robot.getDevice("right wheel motor")

#set motors to velocity mode (or stop them initially)
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))
left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

# Initialize and enable proximity sensors
proximity_sensors = []
sensor_names = [f"ps{i}" for i in range(8)]

for name in sensor_names:
    sensor = param.robot.getDevice(name)
    sensor.enable(param.timestep)
    proximity_sensors.append(sensor)


encoder_left = param.robot.getDevice('left wheel sensor')
encoder_right = param.robot.getDevice('right wheel sensor')
encoder_left.enable(param.timestep)
encoder_right.enable(param.timestep)

# Get the speaker device
speaker = param.robot.getDevice('speaker')

supervisor = Supervisor()

# Get the time step of the current world
timestep = int(supervisor.getBasicTimeStep())

# Get robot node
robot_node = supervisor.getFromDef("EPUCK")

# Get the translation and rotation fields
trans_field = robot_node.getField("translation")
rot_field = robot_node.getField("rotation")


#camera initialization 
camera = param.robot.getDevice('camera')
camera.enable(timestep)

led_ring =[]
for i in range(8):
    led_name=f'led{i}'
    led = param.robot.getDevice(led_name)
    if led:
        led_ring.append(led)

# Test ring LEDs
for led in led_ring:
    led.set(1)  # Turn all LEDs on
