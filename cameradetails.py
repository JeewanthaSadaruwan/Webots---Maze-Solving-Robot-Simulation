
from controller import Robot

robot = Robot()
timestep = int(robot.getBasicTimeStep())

for _ in range(1):                  # wait small time to capture the image
    robot.step(timestep)

#camera initialization 
camera = robot.getDevice('camera')
camera.enable(timestep)

#get camera dimensions and size of the picture
width = camera.getWidth()
height = camera.getHeight()
print(f"camera resolution: {width}x{height}")
bytes_per_pixel = 4  # Assuming RGBA format
image_size = width*height*bytes_per_pixel
print(f"image size: {image_size} bytes")

#capture image
image = camera.getImage()
if image is not None:
    print("Image captured successfully!")
else:
    print("Error: Failed to capture image.")

camera.saveImage("image.png", 100)  # save the image to a file

#process the pixel at (x=10 , y=10 )
red = camera.imageGetRed(image, width, 10, 10)
green = camera.imageGetGreen(image, width, 10, 10)
blue = camera.imageGetBlue(image, width, 10, 10)

print(f"Pixel at (10,10) has RGB values: R={red}, G={green}, B={blue}")

#process the color of the image
for x in range(0, width, 2):
    for y in range(0, height, 2):
        r = camera.imageGetRed(image, width, x, y)
        g = camera.imageGetGreen(image, width, x, y)
        b = camera.imageGetBlue(image, width, x, y)
        # process the pixel data here
        r+=r
        g+=g
        b+=b
        #normalize and determine the dominant color
if r > g and r > b:
    print('red')
elif g > r and g > b:
    print('green')
elif b > r and b > g:
    print('blue')
else:
    print('unknown')

