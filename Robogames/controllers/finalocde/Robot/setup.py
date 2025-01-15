from controller import Robot
from Robot import param


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

