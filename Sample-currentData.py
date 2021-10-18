#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import argparse

from websocket_server import WebsocketServer


def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("--host", type=str, default='192.168.179.11')
    parser.add_argument("--port", type=int, default=8080)

    args = parser.parse_args()

    return args


def event_new_client(client, server):
    client_address = ''
    client_address += str(client['address'][0])
    client_address += ':'
    client_address += str(client['address'][1])

    print('Event New Client ' + client_address)


def event_client_left(client, server):
    client_address = ''
    client_address += str(client['address'][0])
    client_address += ':'
    client_address += str(client['address'][1])

    print('Event Client Left ' + client_address)


def event_message_received(client, server, message):
    json_data = json.loads(message)

    # blinkSpeed(静止指標)：まばたき速度、閉眼時間(mSec)
    # 0-400(通常90−180付近)
    blinkSpeed = json_data.get('blinkSpeed')
    # blinkStrength(静止指標)：まばたき強度(uV-equiv)
    # 0-1000(通常30−150付近)
    blinkStrength = json_data.get('blinkStrength')

    # eyeMoveUp(静止指標) 視線が上に動いた時のイベント
    # 0: 検知無し、1: 極小-7: 特大
    eyeMoveUp = json_data.get('eyeMoveUp')
    # eyeMoveDown(静止指標) 視線が下に動いた時のイベント
    # 0: 検知無し、1: 極小-7: 特大
    eyeMoveDown = json_data.get('eyeMoveDown')
    # eyeMoveLeft(静止指標) 視線が左に動いた時のイベント
    # 0: 検知無し、1: 極小-7: 特大
    eyeMoveLeft = json_data.get('eyeMoveLeft')
    # eyeMoveRight(静止指標) 視線が右に動いた時のイベント
    # 0: 検知無し、1: 極小-7: 特大
    eyeMoveRight = json_data.get('eyeMoveRight')

    # roll：姿勢角のロール成分(左右傾き)を示す度
    # -180.00 ～ 180.00
    roll = json_data.get('roll')
    # pitch：姿勢角のピッチ成分（前後傾き）を示す度
    # -180.00 ～ 180.00
    pitch = json_data.get('pitch')
    # yaw：姿勢角のヨー成分（横回転）を示す度
    # 0.00 ～ 360.00
    yaw = json_data.get('yaw')

    # accX：加速度のX軸成分（左右）1G=16
    # -128(-8G) ～ 127(7.9375G)
    accX = json_data.get('accX')
    # accY：加速度のY軸成分（前後）1G=16
    # -128(-8G) ～ 127(7.9375G)
    accY = json_data.get('accY')
    # accZ：加速度のZ軸成分（上下）1G=16
    # -128(-8G) ～ 127(7.9375G)
    accZ = json_data.get('accZ')

    # walking(isWalking)(歩行指標)：かかとが地面についた時の一歩の検知(検知後0.15~0.25s後にフラグ)
    # 0/false: 検知無し、1/true: 検知有り
    walking = json_data.get('walking')

    # noiseStatus：眼電位電極のノイズ状況を表す整数値
    # 0/false: ノイズ無し、1/true: ノイズ有り
    noiseStatus = json_data.get('noiseStatus')

    # fitError：JINS MEMEが実際に装着されているかどうか、揺れで5秒に1回判定
    # 0: 装着中、1: 非装着
    fitError = json_data.get('fitError')

    # powerLeft：電池残量を表す整数値
    # 0: 充電中、1: 空 ～ 5: 満充電
    powerLeft = json_data.get('powerLeft')

    # sequenceNumber(seqNo)：0-255までの循環連番整数
    sequenceNumber = json_data.get('sequenceNumber')

    print('sequenceNumber:' + str(sequenceNumber))

    print('blinkSpeed:' + str(blinkSpeed))
    print('blinkStrength:' + str(blinkStrength))

    print('eyeMoveUp:' + str(eyeMoveUp))
    print('eyeMoveDown:' + str(eyeMoveDown))
    print('eyeMoveLeft:' + str(eyeMoveLeft))
    print('eyeMoveRight:' + str(eyeMoveRight))

    print('roll:' + str(roll))
    print('pitch:' + str(pitch))
    print('yaw:' + str(yaw))

    print('accX:' + str(accX))
    print('accY:' + str(accY))
    print('accZ:' + str(accZ))

    print('walking:' + str(walking))

    print('noiseStatus:' + str(noiseStatus))

    print('fitError:' + str(fitError))

    print('powerLeft:' + str(powerLeft))


def main():
    args = get_args()

    host = args.host
    port = args.port

    # サーバーインスタンス
    server = WebsocketServer(host=host, port=port)

    # イベントコールバック設定
    server.set_fn_new_client(event_new_client)
    server.set_fn_client_left(event_client_left)
    server.set_fn_message_received(event_message_received)

    # サーバー起動
    server.run_forever()


if __name__ == "__main__":
    main()
