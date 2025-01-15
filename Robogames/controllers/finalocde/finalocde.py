
import Robot.param
from Robot import calibration
from Robot import Sensor
from Robot import navigation
from Robot import setup
from Robot import Control


def main():
    #navigation.wallfollowing()
    #print(Sensor.encoderValues())
    #Control.turn180()
    # calibration.distanceSensorCalibration()
    # Control.moveForwardwithPD()
    # Control.moveForward()
    # Control.moveBackward()
    # Control.turnleft()
    Control.movedistance(0.25)
main()