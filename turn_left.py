import sys
import time
import math
from pyroombaadapter import PyRoombaAdapter

PORT = "/dev/ttyACM0"
adapter = PyRoombaAdapter(PORT)

args = sys.argv
deg = int(args[1])

adapter.move(0.0, math.radians(deg))  # go straight
time.sleep(1.0)
