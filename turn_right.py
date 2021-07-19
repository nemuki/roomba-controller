import sys
import time
import math
from pyroombaadapter import PyRoombaAdapter


def main(deg):
    PORT = "/dev/ttyACM0"
    adapter = PyRoombaAdapter(PORT)

    adapter.move(0.0, math.radians(deg))  # go straight
    time.sleep(1.0)


if __name__ == "__main__":
    args = sys.argv
    deg = int(args[1])
    main(deg)
