from controller import Robot
from Robot import param
from Robot import setup

class Sensor:

    def distanceSensorValues():                                             #takes the values at one instance
        
        param.robot.step(param.timestep)
        sensor_values = [sensor.getValue() for sensor in setup.proximity_sensors]
        return sensor_values
    
    def encoderValues():
        encoder_readings =[setup.encoder_left.getValue(),setup.encoder_right.getValue()]
        return encoder_readings
    



    
    

        

    