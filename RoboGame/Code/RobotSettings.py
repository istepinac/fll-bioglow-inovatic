
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction

# Define the robot's motors and drive base

hub = PrimeHub()
left_motor = Motor(Port.A)
right_motor = Motor(Port.B)
left_hand_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
right_hand_motor = Motor(Port.D, Direction.COUNTERCLOCKWISE)
drive_base = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=114)
color_sensor = ColorSensor(Port.S1)

drive_base.settings(straight_speed=100, straight_acceleration=200, turn_rate=100, turn_acceleration=200)

