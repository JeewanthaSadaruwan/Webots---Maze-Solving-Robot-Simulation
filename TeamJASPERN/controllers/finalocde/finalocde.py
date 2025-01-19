from Robot import param
from Robot import calibration
from Robot import Sensor
from Robot import setup
from Robot import maze


def main():
    
    calibration.distanceSensorCalibration()
    maze.final()
    
main()