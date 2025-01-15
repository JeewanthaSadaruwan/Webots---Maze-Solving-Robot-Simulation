from controller import Robot
import numpy as np

robot = Robot()
timestep = int(robot.getBasicTimeStep())
camera = robot.getDevice('camera')
camera.enable(timestep)

#define color thresholds(adjust as needed)

colors = {
    'Red': (255 , 0 ,0),
    'Yellow': (255, 255, 0),
    'pink': (255, 0, 255),
    'brown': (165, 105, 30),
    'green': (0, 255, 0)
}

def color_match(pixel, target_color, tolerance=30):
    return(abs(pixel[0] - target_color[0]) < tolerance and
           abs(pixel[1] - target_color[1]) < tolerance and
           abs(pixel[2] - target_color[2]) < tolerance)

for _ in range(1):
    robot.step(timestep)    

image = camera.getImage()

width = camera.getWidth()
height = camera.getHeight()

for x in range(0, width, 2):
    for y in range(0, height, 2):
        red = camera.imageGetRed(image, width, x, y)
        green = camera.imageGetGreen(image, width, x, y)
        blue = camera.imageGetBlue(image, width, x, y)

        pixel = (red, green, blue)
        print(pixel)

        for color_name, target_color in colors.items():
            if color_match(pixel, target_color):
                print(f"Pixel at ({x},{y}) matches color: {color_name}")
                break
            else:
                print(f"Pixel at ({x},{y}) does not match any color")