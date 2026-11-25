from RobotSettings import *

#Base: drone survey

Robot.settings(straight_speed=200)
Robot.straight(700)

Robot.settings(straight_speed=800)
Robot.curve(250,-45)