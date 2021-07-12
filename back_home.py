import time
from pyroombaadapter import PyRoombaAdapter

PORT = "/dev/ttyACM0"
adapter = PyRoombaAdapter(PORT)

adapter.start_seek_dock()
time.sleep(1.0)
