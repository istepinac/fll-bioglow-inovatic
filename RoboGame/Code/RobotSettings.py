
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
from pybricks.parameters import Port, Direction, Stop


# Define the robot's motors and drive base

hub = PrimeHub()
left_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.F, Direction.CLOCKWISE)
left_hand_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_hand_motor = Motor(Port.E, Direction.COUNTERCLOCKWISE)
Robot = DriveBase(left_motor, right_motor, wheel_diameter=62.4, axle_track=160)
color_sensor = ColorSensor(Port.C)
Robot.use_gyro(True)
Robot.settings(straight_speed=800, straight_acceleration=600, turn_rate=200, turn_acceleration=400)
