# Roomba Controller

中学生1日体験用のプログラム

## 実行環境

```
Python 3.6.x or higher (2.7 is not supported)
```

## セットアップ

```sh
$ git clone https://github.com/nemuki/roomba-controller.git
$ cd roomba-controller
$ pip3 install -r requirements.txt
```

## それぞれの動作

- `go_straight.py`
  - コマンドライン引数で `1~5` の値を指定すると前に動く

- `turn_right.py`
  - コマンドライン引数で `0~360` の値を指定すると右に回る

- `turn_left.py`
  - コマンドライン引数で `0~360` の値を指定すると左に回る

- `back_home.py`
  - ホームベースへ戻る

- `darth_bader.py`
  - ダースベイダーのテーマが流れる