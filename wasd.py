import os
import sys
import termios
import time
import fcntl
from time import sleep
import math
from pyroombaadapter import PyRoombaAdapter

PORT = "/dev/ttyACM0"
adapter = PyRoombaAdapter(PORT)

MAX_FORWARD = 40  # in cm per second
MAX_ROTATION = 180  # in cm per second


class Key:
    def key_get(self, non_blocking):
        if non_blocking:
            # 標準入力のファイルディスクリプタを取得
            self.fd = sys.stdin.fileno()

            # fdの端末属性をゲットする
            # oldとnewには同じものが入る。
            # newに変更を加えて、適応する
            # oldは、後で元に戻すため
            self.old = termios.tcgetattr(self.fd)
            self.new = termios.tcgetattr(self.fd)

            # new[3]はlflags
            # ICANON(カノニカルモードのフラグ)を外す
            self.new[3] &= ~termios.ICANON
            # ECHO(入力された文字を表示するか否かのフラグ)を外す
            self.new[3] &= ~termios.ECHO

            try:
                self.fcntl_old = fcntl.fcntl(self.fd, fcntl.F_GETFL)
                fcntl.fcntl(self.fd, fcntl.F_SETFL, self.fcntl_old |
                            os.O_NONBLOCK)

                # 書き換えたnewをfdに適応する
                termios.tcsetattr(self.fd, termios.TCSANOW, self.new)
                # キーボードから入力を受ける。
                # lfalgsが書き換えられているので、エンターを押さなくても次に進む。echoもしない
                self.ch = sys.stdin.read(1)
            finally:
                fcntl.fcntl(self.fd, fcntl.F_SETFL, self.fcntl_old)
                # fdの属性を元に戻す
                # 具体的にはICANONとECHOが元に戻る
                termios.tcsetattr(self.fd, termios.TCSANOW, self.old)
            return self.ch
        else:
            self.fd = sys.stdin.fileno()
            self.old = termios.tcgetattr(self.fd)
            self.new = termios.tcgetattr(self.fd)
            self.new[3] &= ~termios.ICANON
            self.new[3] &= ~termios.ECHO
            try:
                termios.tcsetattr(self.fd, termios.TCSANOW, self.new)
                self.ch = sys.stdin.read(1)
            finally:
                termios.tcsetattr(self.fd, termios.TCSANOW, self.old)
            return self.ch

    def key_control(self, throttle, steer, non_blocking = True):
        self._key = self.key_get(non_blocking)
        if self._key == 'w':  # throttle up
            throttle += 1
        elif self._key == 'a':  # right
            steer += 1
        elif self._key == 's':  # throttle down
            throttle -= 1
        elif self._key == 'd':  # left
            steer -= 1

        return throttle, steer


    def run(self, throttle, steer):
        FWD_SPEED = MAX_FORWARD / 2
        ROT_SPEED = MAX_ROTATION / 2

        adapter.move(throttle * FWD_SPEED, steer * ROT_SPEED)
        # time.sleep(0.1)


if __name__ == '__main__':
    throttle = 0
    steer = 0
    non_blocking = True
    key = Key()
    print('start')
    while True:
        throttle, steer = key.key_control(throttle, steer, non_blocking)
        key.run(throttle, steer)

