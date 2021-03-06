from time import sleep
from pyroombaadapter import PyRoombaAdapter


def main():
    PORT = "/dev/ttyACM0"
    adapter = PyRoombaAdapter(PORT)

    adapter.send_song_cmd(0, 9,
                        [69, 69, 69, 65, 72, 69, 65, 72, 69],
                        [40, 40, 40, 30, 10, 40, 30, 10, 80])
    adapter.send_play_cmd(0)
    sleep(10.0)


if __name__ == "__main__":
    main()