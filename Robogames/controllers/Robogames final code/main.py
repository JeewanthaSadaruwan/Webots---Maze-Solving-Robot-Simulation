from controller import Robot

robot = Robot()
timestep = int(robot.getBasicTimeStep())

proximity_sensors = []

for i in range(8):
    sensor = robot.getDevice(f"ps{i}")
    sensor.enable(timestep)
    proximity_sensors.append(sensor)

print(proximity_sensors)