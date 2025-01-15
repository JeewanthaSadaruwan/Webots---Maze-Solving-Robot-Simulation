from controller import Robot
from Robot import param
from Robot import Sensor
from Robot import setup




class calibration:
    desired_distance = [0.0]*8
    def distanceSensorCalibration():

        temp_distance = [0.0]*8
        for i in range(10):
            param.robot.step(param.timestep)
            sensor_values = Sensor.distanceSensorValues()
            for i in range(8):
                temp_distance[i] += sensor_values[i]
            
        calibration.desired_distance = [x/10 for x in temp_distance]

        # If you have stereo speakers, pass both left and right
        setup.speaker.playSound(
            left=setup.speaker,
            right=setup.speaker,
            sound=param.calibration_sound,
            volume=param.volume,
            pitch=param.pitch,
            balance=param.balance,
            loop=param.loop
        )

        param.robot.step(3000)  # Wait for 2 seconds
        print("distance sensor calibration is successful")
        print(calibration.desired_distance)
        return calibration.desired_distance