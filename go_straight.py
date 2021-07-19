import sys
import time
import math
from pyroombaadapter import PyRoombaAdapter


def main(sec):
    PORT = "/dev/ttyACM0"
    adapter = PyRoombaAdapter(PORT)

    for i in range(sec):
        adapter.move(1, math.radians(0.0))  # go straight
        time.sleep(1.0)


if __name__ == "__main__":
    args = sys.argv
    sec = int(args[1])
    main(sec)
