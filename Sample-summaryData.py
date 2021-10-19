#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import socket
import argparse

from websocket_server import WebsocketServer


def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("--host", type=str, default=None)
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

    # date：日付
    # 1970-01-01T09:00:00 - 2106-02-07T06:28:16
    date = json_data.get('date')

    # validDuration val_s：測定秒数(s)
    # 0.00-60.00
    validDuration = json_data.get('validDuration')

    # noiseDuration nis_s：電極ノイズ秒数(s)
    # 0.00-60.00
    noiseDuration = json_data.get('noiseDuration')

    # fitDuration wea_s：装着秒数(s)
    # 0.00-60.00
    fitDuration = json_data.get('fitDuration')

    # walkingDuration stp_s：歩行秒数(s)
    # 0.00-60.00
    walkingDuration = json_data.get('walkingDuration')

    # powerLeft：電池残量を表す整数値
    # 0: 充電中、1: 空 ～ 5: 満充電
    powerLeft = json_data.get('powerLeft')

    # eyeMoveHorizontal(静止指標) ems_rl：視線移動小回数(左右)
    # 0-255
    eyeMoveHorizontal = json_data.get('eyeMoveHorizontal')
    # eyeMoveVertical(静止指標) ems_ud：視線移動小回数(上下)
    # 0-255
    eyeMoveVertical = json_data.get('eyeMoveVertical')
    # eyeMoveBigHorizontal(静止指標) eml_rl：視線移動大回数(左右)
    # 0-255
    eyeMoveBigHorizontal = json_data.get('eyeMoveBigHorizontal')
    # eyeMoveBigVertical(静止指標) eml_ud：視線移動大回数(上下)
    # 0-255
    eyeMoveBigVertical = json_data.get('eyeMoveBigVertical')

    # headMoveVerticalCount hm_po 首フリ回数縦
    # 0-255
    headMoveVerticalCount = json_data.get('headMoveVerticalCount')
    # headMoveHorizontalCount hm_yo 首フリ回数横
    # 0-255
    headMoveHorizontalCount = json_data.get('headMoveHorizontalCount')

    # walkingVibrationRightX(歩行指標) sa_xr：歩行振動X (cm, 右足)
    # 0.00-16.00
    walkingVibrationRightX = json_data.get('walkingVibrationRightX')
    # walkingVibrationLeftX(歩行指標) sa_xl：歩行振動X (cm, 左足)
    # 0.00-16.00
    walkingVibrationLeftX = json_data.get('walkingVibrationLeftX')
    # walkingVibrationRightY(歩行指標) sa_yr：歩行振動Y (cm, 右足)
    # 0.00-16.00
    walkingVibrationRightY = json_data.get('walkingVibrationRightY')
    # walkingVibrationLeftY(歩行指標) sa_yl：歩行振動Y (cm, 左足)
    # 0.00-16.00
    walkingVibrationLeftY = json_data.get('walkingVibrationLeftY')
    # walkingVibrationRightZ(歩行指標) sa_zr：歩行振動Z (cm, 右足)
    # 0.00-16.00
    walkingVibrationRightZ = json_data.get('walkingVibrationRightZ')
    # walkingVibrationLeftZ(歩行指標) sa_zl：歩行振動Z (cm, 左足)
    # 0.00-16.00
    walkingVibrationLeftZ = json_data.get('walkingVibrationLeftZ')

    # landingStrengthRightMaxAvg(歩行指標) st_r：最大着地強度平均 (G, 右足)
    # 0.00-8.00
    landingStrengthRightMaxAvg = json_data.get('landingStrengthRightMaxAvg')
    # landingStrengthLeftMaxAvg(歩行指標) st_l：最大着地強度平均 (G, 左足)
    # 0.00-8.00
    landingStrengthLeftMaxAvg = json_data.get('landingStrengthLeftMaxAvg')

    # slopeXAvg tl_xav：傾き平均X (度)
    # -180.00-180.00
    slopeXAvg = json_data.get('slopeXAvg')
    # slopeYAvg tl_yav：傾き平均Y (度)
    # -180.00-180.00
    slopeYAvg = json_data.get('slopeYAvg')
    # slopeXStd tl_xsd：傾き標準偏差X (度)
    # 0-655.36
    slopeXStd = json_data.get('slopeXStd')
    # slopeYStd tl_ysd：傾き標準偏差Y (度)
    # 0-655.36
    slopeYStd = json_data.get('slopeYStd')

    # highSpeedStepsNum(歩行指標) stp_fst：歩行時歩数（高速 280-370ms）
    # 0-255
    highSpeedStepsNum = json_data.get('highSpeedStepsNum')
    # middleSpeedStepsNum(歩行指標) stp_mid：歩行時歩数（中速 380-440ms）
    # 0-255
    middleSpeedStepsNum = json_data.get('middleSpeedStepsNum')
    # lowSpeedStepsNum(歩行指標) stp_slw：歩行時歩数（低速 450-590ms）
    # 0-255
    lowSpeedStepsNum = json_data.get('lowSpeedStepsNum')
    # ultraLowSpeedStepsNum(歩行指標) stp_vsl：歩行時歩数（超低速 600-1000ms）
    # 0-255
    ultraLowSpeedStepsNum = json_data.get('ultraLowSpeedStepsNum')

    # nptAvgWeak(静止指標) クレンジング弱 lc_npt_av NPT：実効まばたき速度(平均)
    # -0.256 - 0.256
    nptAvgWeak = json_data.get('nptAvgWeak')
    # weakBlinkSpeedAvg(静止指標) クレンジング弱 lc_bkw_av：まばたき速度平均(mSec)
    # 50-306
    weakBlinkSpeedAvg = json_data.get('weakBlinkSpeedAvg')
    # weakBlinkSpeedStd(静止指標) クレンジング弱 lc_bkw_sd：まばたき速度標準偏差(mSec)
    # 0-51.2
    weakBlinkSpeedStd = json_data.get('weakBlinkSpeedStd')
    # weakBlinkStrengthAvg(静止指標) クレンジング弱 lc_bkh_av：まばたき強度平均(uV-equiv)
    # 0-512
    weakBlinkStrengthAvg = json_data.get('weakBlinkStrengthAvg')
    # weakBlinkStrengthStd(静止指標) クレンジング弱 lc_bkh_sd：まばたき強度標準偏差(uV-equiv)
    # 0-51.2
    weakBlinkStrengthStd = json_data.get('weakBlinkStrengthStd')
    # weakBlinkCount(静止指標) クレンジング弱 lc_bk_n：まばたき回数
    # 0-255
    weakBlinkCount = json_data.get('weakBlinkCount')
    # weakBlinkSwarmCount(静止指標) クレンジング弱 lc_bkg_n：1s以内に複数回まばたきが発生した回数
    # 0-255
    weakBlinkSwarmCount = json_data.get('weakBlinkSwarmCount')
    # weakBlinkIntervalAvg(静止指標) クレンジング弱 lc_bki_av：まばたき間隔秒数平均(s)
    # 0-51.2
    weakBlinkIntervalAvg = json_data.get('weakBlinkIntervalAvg')
    # weakBlinkIntervalCount(静止指標) クレンジング弱 lc_bki_n：まばたき間隔回数
    # 0-255
    weakBlinkIntervalCount = json_data.get('weakBlinkIntervalCount')

    # nptAvgStrong(静止指標) クレンジング強 sc_npt_av NPT： 実効まばたき速度(平均)
    # -0.256 - 0.256
    nptAvgStrong = json_data.get('nptAvgStrong')
    # strongBlinkSpeedAvg(静止指標) クレンジング強 sc_bkw_av：まばたき速度平均(mSec)
    # 50-306
    strongBlinkSpeedAvg = json_data.get('strongBlinkSpeedAvg')
    # strongBlinkSpeedStd(静止指標) クレンジング強 sc_bkw_sd：まばたき速度標準偏差(mSec)
    # 0-51.2
    strongBlinkSpeedStd = json_data.get('strongBlinkSpeedStd')
    # strongBlinkStrengthAvg(静止指標) クレンジング強 sc_bkh_av：まばたき強度平均(uV-equiv)
    # 0-512
    strongBlinkStrengthAvg = json_data.get('strongBlinkStrengthAvg')
    # strongBlinkStrengthStd(静止指標) クレンジング強 sc_bkh_sd：まばたき強度標準偏差(uV-equiv)
    # 0-51.2
    strongBlinkStrengthStd = json_data.get('strongBlinkStrengthStd')
    # strongBlinkCount(静止指標) クレンジング強 sc_bk_n：まばたき回数
    # 0-255
    strongBlinkCount = json_data.get('strongBlinkCount')
    # strongBlinkSwarmCount(静止指標) クレンジング強 sc_bkg_n：1s以内に複数回まばたきが発生した回数
    # 0-255
    strongBlinkSwarmCount = json_data.get('strongBlinkSwarmCount')
    # strongBlinkIntervalAvg(静止指標) クレンジング強 sc_bki_av：まばたき間隔秒数平均(s)
    # 0-51.2
    strongBlinkIntervalAvg = json_data.get('strongBlinkIntervalAvg')
    # strongBlinkIntervalCount(静止指標) クレンジング強 sc_bki_n：まばたき間隔回数
    # 0-255
    strongBlinkIntervalCount = json_data.get('strongBlinkIntervalCount')

    print('date:' + str(date))

    print('validDuration:' + str(validDuration))
    print('noiseDuration:' + str(noiseDuration))
    print('fitDuration:' + str(fitDuration))
    print('walkingDuration:' + str(walkingDuration))

    print('powerLeft:' + str(powerLeft))

    print('eyeMoveHorizontal:' + str(eyeMoveHorizontal))
    print('eyeMoveVertical:' + str(eyeMoveVertical))
    print('eyeMoveBigHorizontal:' + str(eyeMoveBigHorizontal))
    print('eyeMoveBigVertical:' + str(eyeMoveBigVertical))

    print('headMoveVerticalCount:' + str(headMoveVerticalCount))
    print('headMoveHorizontalCount:' + str(headMoveHorizontalCount))

    print('walkingVibrationRightX:' + str(walkingVibrationRightX))
    print('walkingVibrationLeftX:' + str(walkingVibrationLeftX))
    print('walkingVibrationRightY:' + str(walkingVibrationRightY))
    print('walkingVibrationLeftY:' + str(walkingVibrationLeftY))
    print('walkingVibrationRightZ:' + str(walkingVibrationRightZ))
    print('walkingVibrationLeftZ:' + str(walkingVibrationLeftZ))

    print('landingStrengthRightMaxAvg:' + str(landingStrengthRightMaxAvg))
    print('landingStrengthLeftMaxAvg:' + str(landingStrengthLeftMaxAvg))

    print('slopeXAvg:' + str(slopeXAvg))
    print('slopeYAvg:' + str(slopeYAvg))
    print('slopeXStd:' + str(slopeXStd))
    print('slopeYStd:' + str(slopeYStd))

    print('dahighSpeedStepsNumte:' + str(highSpeedStepsNum))
    print('middleSpeedStepsNum:' + str(middleSpeedStepsNum))
    print('lowSpeedStepsNum:' + str(lowSpeedStepsNum))
    print('ultraLowSpeedStepsNum:' + str(ultraLowSpeedStepsNum))

    print('nptAvgWeak:' + str(nptAvgWeak))
    print('weakBlinkSpeedAvg:' + str(weakBlinkSpeedAvg))
    print('weakBlinkSpeedStd:' + str(weakBlinkSpeedStd))
    print('weakBlinkStrengthAvg:' + str(weakBlinkStrengthAvg))
    print('weakBlinkStrengthStd:' + str(weakBlinkStrengthStd))
    print('weakBlinkCount:' + str(weakBlinkCount))
    print('weakBlinkSwarmCount:' + str(weakBlinkSwarmCount))
    print('weakBlinkIntervalAvg:' + str(weakBlinkIntervalAvg))
    print('weakBlinkIntervalCount:' + str(weakBlinkIntervalCount))

    print('nptAvgStrong:' + str(nptAvgStrong))
    print('strongBlinkSpeedAvg:' + str(strongBlinkSpeedAvg))
    print('strongBlinkSpeedStd:' + str(strongBlinkSpeedStd))
    print('strongBlinkStrengthAvg:' + str(strongBlinkStrengthAvg))
    print('strongBlinkStrengthStd:' + str(strongBlinkStrengthStd))
    print('strongBlinkCount:' + str(strongBlinkCount))
    print('strongBlinkSwarmCount:' + str(strongBlinkSwarmCount))
    print('strongBlinkIntervalAvg:' + str(strongBlinkIntervalAvg))
    print('strongBlinkIntervalCount:' + str(strongBlinkIntervalCount))


def main():
    args = get_args()

    host = args.host
    port = args.port

    if host is None:
        host = socket.gethostbyname(socket.gethostname())

    print('Server ' + str(host) + ':' + str(port))

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
