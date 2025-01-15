
from controller import Robot
from Robot import Sensor
from Robot import param
from Robot import setup



class navigation:
    
    def wallfollowing():
        while param.robot.step(param.timestep) != -1:
            #Read sensor values 
            sensor_values = Sensor.distanceSensorValues()
            encoder_values = Sensor.encoderValues()
            #print(sensor_values)
            print(encoder_values)
            
            front_right = sensor_values[0]
            front_left = sensor_values[7]
            left = sensor_values[5]
            right = sensor_values[2]
            
            if front_left > param.THRESHOLD or front_right > param.THRESHOLD:
                #obstacle in front , turn right
                setup.left_motor.setVelocity(param.SPEED)
                setup.right_motor.setVelocity(param.SPEED/2)
            elif left < param.THRESHOLD:
                #no wall on the left,turn left
                setup.left_motor.setVelocity(param.SPEED/2)
                setup.right_motor.setVelocity(param.SPEED)
            else:
                #wall on the left , move forward
                setup.left_motor.setVelocity(param.SPEED)
                setup.right_motor.setVelocity(param.SPEED)



        