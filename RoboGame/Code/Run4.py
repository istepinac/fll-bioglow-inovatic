from RobotSettings import *

#Base: tangled and research platform


Robot.straight(400)
Robot.turn(45)
Robot.straight(356)
Robot.turn(-45)
right_hand_motor.run_until_stalled(300, then=Stop.HOLD, duty_limit=40)
right_hand_motor.run_angle(-300, 40)
Robot.straight(60)
right_hand_motor.run_angle(-300, 70, wait=False)
wait(500)
Robot.straight(-60)
right_hand_motor.run_angle(-300, 200, wait=False)
Robot.turn(-13)
Robot.settings(straight_speed=800, straight_acceleration=900)
Robot.straight(300)
Robot.straight(-70)
Robot.straight(300)
Robot.straight(-100)

