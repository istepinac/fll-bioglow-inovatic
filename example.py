from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import run_task, wait

hub = PrimeHub()
motor = Motor(Port.A)


async def spin_motor():
    await motor.run_angle(300, 180)


async def main():
    await spin_motor()
    await wait(1000)


run_task(main())