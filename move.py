import os
import sys
import termios
import fcntl
from time import sleep
import math
from pyroombaadapter import PyRoombaAdapter

PORT = "/dev/ttyACM0"
adapter = PyRoombaAdapter(PORT)
adapter.move(-0.2, math.radians(0.0))  # go straight
sleep(1.0)
adapter.move(0, math.radians(-30))  # turn right
sleep(6.0)
adapter.move(0.2, math.radians(0.0))  # go straight
sleep(1.0)
adapter.move(0, math.radians(20))  # turn left

MAX_FORWARD = 50  # in cm per second
MAX_ROTATION = 200  # in cm per second
SPEED_INC = 10  # increment in percent

robot.go(robot_dir * FWD_SPEED, robot_rot * ROT_SPEED)
time.sleep(0.1)

FWD_SPEED = MAX_FORWARD / 2
ROT_SPEED = MAX_ROTATION / 2

while True:
    if self._key == 'w' and throttle < 1000:  # throttle up
        robot_dir += 1
        update_roomba = True
    if self._key == 'a' and steer < 100:  # right
        robot_rot += 1
        update_roomba = True
    if self._key == 's' and throttle > -1000:  # throttle down
        robot_dir -= 1
        update_roomba = True
    if self._key == 'd' and steer > -100:  # left
        robot_rot -= 1
        update_roomba = True
