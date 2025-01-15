from controller import Robot, Camera, Motor


#initialize the robot
robot = Robot()                                                   
time_step = int(robot.getBasicTimeStep())

#motor initialization
left_Motor = robot.getDevice('left wheel motor')
right_Motor = robot.getDevice('right wheel motor')
left_Motor.setPosition(float('inf'))
right_Motor.setPosition(float('inf'))
left_Motor.setVelocity(0.0)
right_Motor.setVelocity(0.0)

#camera initialization
camera = robot.getDevice('camera')
camera.enable(time_step)

#color targets in sequence
color_sequence = ['red', 'yellow', 'pink', 'brown', 'green']
current_target_index = 0


#function to get the color of the target
def detect_color(image):
    width = camera.getWidth()
    height = camera.getHeight()
    red , green, blue = 0, 0, 0
    for x in range(0, width, 2):
        for y in range(0, height, 2):
            r = Camera.imageGetRed(image, width, x, y)
            g = Camera.imageGetGreen(image, width, x, y)
            b = Camera.imageGetBlue(image, width, x, y)
            red += r
            green += g
            blue += b

            #normalize and determine the dominant color

            if red > green and red > blue:
                return 'red'
            elif green > red and green > blue:
                return 'green'
            elif blue > red and blue > green:
                return 'blue'

            return "unknown"

#function to move the robot forward
