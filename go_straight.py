import sys
import time
import math
from pyroombaadapter import PyRoombaAdapter

PORT = "/dev/ttyACM0"
adapter = PyRoombaAdapter(PORT)

args = sys.argv
sec = int(args[1])

for i in range(sec):
    adapter.move(1, math.radians(0.0))  # go straight
    time.sleep(1.0)
