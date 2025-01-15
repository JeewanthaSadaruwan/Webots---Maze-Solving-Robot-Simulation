from controller import Robot
from Robot import calibration
from Robot import param
from Robot import setup
from Robot import Sensor

import math


class Control:

    def errorCompute(desired, actual):
        error = desired - actual
        derivative = error - param.previous_error
        param.previous_error = error

        return param.forward_kp * error + param.forward_kp * derivative

    def moveForwardwithPD():

        
        desired_distances = calibration.desired_distance
        
        while param.robot.step(param.timestep) != -1:

            # Get current sensor readings
            actual_distances = Sensor.distanceSensorValues()
            
            # Calculate corrections based on front sensors
            left_correction = Control.errorCompute(desired_distances[2],actual_distances[2])
            right_correction = Control.errorCompute(desired_distances[5],actual_distances[5])
            print(left_correction,right_correction)
             # Adjust motor speeds
            left_speed = param.SPEED - left_correction
            right_speed = param.SPEED - right_correction

            setup.left_motor.setVelocity(left_speed)
            setup.right_motor.setVelocity(right_speed)


    def moveForward():
        setup.left_motor.setVelocity(param.SPEED)
        setup.right_motor.setVelocity(param.SPEED)

    def moveBackward():
        setup.left_motor.setVelocity(-param.SPEED)
        setup.right_motor.setVelocity(-param.SPEED)

    # def moveBit():

    def calculateTargetDistance(distance):
        wheel_circumference = 2 * math.pi * param.wheelRadius
        target_rotation = (distance / wheel_circumference) * 2 * math.pi  # Convert distance to radians\
        return target_rotation

    def movedistance(distance):
        param.robot.step(param.timestep)
        target_rotation = Control.calculateTargetDistance(distance)
        # Loop until the target distance is reached
        initial_reading = Sensor.encoderValues()
        
        while param.robot.step(param.timestep) != -1:
            
            setup.left_motor.setVelocity(param.SPEED)
            setup.right_motor.setVelocity(param.SPEED)

            # Get current encoder readings
            current_reading = Sensor.encoderValues()

            #check if rotation is complete
            delta_left = abs(current_reading[0] - initial_reading[0])
            delta_right = abs(current_reading[1] - initial_reading[1])

            if delta_left >= target_rotation and delta_right >= target_rotation:
                #stop the motors
                setup.left_motor.setVelocity(0)
                setup.right_motor.setVelocity(0)
                break


            



    def calculateTargetRotation(turning_angle):
        arc_lenngth = math.pi * param.wheelBase * turning_angle / 360
        target_rotation = arc_lenngth / param.wheelRadius
        return target_rotation
    
    
    def turnleft():

        param.robot.step(param.timestep)
        target_rotation = Control.calculateTargetRotation(90)
        
        initial_reading = Sensor.encoderValues()
        
        while param.robot.step(param.timestep) != -1:
            setup.left_motor.setVelocity(-param.SPEED)
            setup.right_motor.setVelocity(param.SPEED)
            current_reading = Sensor.encoderValues()

            #check if rotation is complete
            delta_left = abs(current_reading[0] - initial_reading[0])
            delta_right = abs(current_reading[1] - initial_reading[1])

            if delta_left >= target_rotation and delta_right >= target_rotation:
                #stop the motors
                setup.left_motor.setVelocity(0)
                setup.right_motor.setVelocity(0)
                break
        
    def turnright():
        param.robot.step(param.timestep)
        target_rotation = Control.calculateTargetRotation(90)
        
        initial_reading = Sensor.encoderValues()
        
        while param.robot.step(param.timestep) != -1:
            setup.left_motor.setVelocity(param.SPEED)
            setup.right_motor.setVelocity(-param.SPEED)
            current_reading = Sensor.encoderValues()

            #check if rotation is complete
            delta_left = abs(current_reading[0] - initial_reading[0])
            delta_right = abs(current_reading[1] - initial_reading[1])

            if delta_left >= target_rotation and delta_right >= target_rotation:
                #stop the motors
                setup.left_motor.setVelocity(0)
                setup.right_motor.setVelocity(0)
                break


    def turn180():
        param.robot.step(param.timestep)                         ########simple issue in here i have to use 200 instead of 180
        target_rotation = Control.calculateTargetRotation(200)    
        
        initial_reading = Sensor.encoderValues()
        
        while param.robot.step(param.timestep) != -1:
            setup.left_motor.setVelocity(param.SPEED)
            setup.right_motor.setVelocity(-param.SPEED)
            current_reading = Sensor.encoderValues()

            #check if rotation is complete
            delta_left = abs(current_reading[0] - initial_reading[0])
            delta_right = abs(current_reading[1] - initial_reading[1])

            if delta_left >= target_rotation and delta_right >= target_rotation:
                #stop the motors
                setup.left_motor.setVelocity(0)
                setup.right_motor.setVelocity(0)
                break
       


