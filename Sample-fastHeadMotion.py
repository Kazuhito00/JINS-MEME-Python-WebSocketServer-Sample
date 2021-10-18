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

    # date：イベント発生日時
    # 1970-01-01 09:00:00 - 2106-02-07 06:28:16
    date = json_data.get('date')
    # type：発生イベント種類
    # fastHeadMotion(固定値)
    type = json_data.get('type')
    # subType：向き
    # right, left, up, down
    subType = json_data.get('subType')
    # value：回数(片道で1)
    # 1-65535
    value = json_data.get('value')

    print('date:' + str(date))
    print('type:' + str(type))
    print('subType:' + str(subType))
    print('value:' + str(value))


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
