import time
from pyroombaadapter import PyRoombaAdapter


def main():
    PORT = "/dev/ttyACM0"
    adapter = PyRoombaAdapter(PORT)

    adapter.start_seek_dock()
    time.sleep(1.0)


if __name__ == "__main__":
    main()
