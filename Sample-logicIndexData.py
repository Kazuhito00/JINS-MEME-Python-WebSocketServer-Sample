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
    print(message)
    json_data = json.loads(message)

    # date：日付
    # 2000-01-01T00:00:00 - 2099-12-31T23:59:59
    date = json_data.get('date')

    # stepCount((歩行指標))：歩数
    # 0-255
    stepCount = json_data.get('stepCount')
    # stepCadence(歩行指標)：ケイデンス(ピッチ)
    # 0-255
    stepCadence = json_data.get('stepCadence')

    # isStill isl：静止（装着してない）判定
    # true: 非装着（静止） false: 装着中（非静止）
    isStill = json_data.get('isStill')

    # betteryLevel：バッテリーレベル
    # 0: 充電中、1: 空 ～ 5: 満充電
    betteryLevel = json_data.get('betteryLevel')

    # noiseTime nis_time：ノイズ時間
    # 0.00 - 15.00
    noiseTime = json_data.get('noiseTime')
    # isValid vld：静止状態のデータ有効性（ノイズ3秒以下かつ歩数5歩以下）
    # true: 有効 false: 無効
    isValid = json_data.get('isValid')

    # xMean tl_yav：傾き平均X (度)
    # -180.00-180.00
    xMean = json_data.get('xMean')
    # xSD Ntl_ysd：傾き平均X (度)
    # -180.00-180.00
    xSD = json_data.get('xSD')
    # yMean tl_xav：傾き標準偏差Y (度)
    # 0-655.36
    yMean = json_data.get('yMean')
    # ySD tl_xsd：傾き標準偏差Y (度)
    # 0-655.36
    ySD = json_data.get('ySD')

    # pitchOnewayCount Nhm_po：首フリ縦回数
    # 0-255
    pitchOnewayCount = json_data.get('pitchOnewayCount')
    # pitchRoundCount hm_pr：ゆっくりな首の傾斜前後回数
    # 0-255
    pitchRoundCount = json_data.get('pitchRoundCount')
    # yawOnewayCount hm_yo：首フリ横回数
    # 0-255
    yawOnewayCount = json_data.get('yawOnewayCount')
    # yawRoundCount hm_yr：ゆっくりな首の傾斜左右回数
    # 0-255
    yawRoundCount = json_data.get('yawRoundCount')

    # xRightStepAmplitude(歩行指標) sa_xr：歩行振動X（cm,右足）
    # 0.00-16.00
    xRightStepAmplitude = json_data.get('xRightStepAmplitude')
    # xLeftStepAmplitude(歩行指標) sa_xl：歩行振動X（cm,左足）
    # 0.00-16.00
    xLeftStepAmplitude = json_data.get('xLeftStepAmplitude')
    # yRightStepAmplitude(歩行指標) sa_yr：歩行振動Y（cm,右足）
    # 0.00-16.00
    yRightStepAmplitude = json_data.get('yRightStepAmplitude')
    # yLeftStepAmplitude(歩行指標) sa_yl：歩行振動Y（cm,左足）
    # 0.00-16.00
    yLeftStepAmplitude = json_data.get('yLeftStepAmplitude')
    # zRightStepAmplitude(歩行指標) sa_zr：歩行振動Z（cm,右足）
    # 0.00-16.00
    zRightStepAmplitude = json_data.get('zRightStepAmplitude')
    # zLeftStepAmplitude(歩行指標) sa_zl：歩行振動Z（cm,左足）
    # 0.00-16.00
    zLeftStepAmplitude = json_data.get('zLeftStepAmplitude')
    # zLeftStepAmplitudeCal(歩行指標) sa_zrc：歩行振動Z補正有（cm,右足）
    # 0.00-20.00
    zLeftStepAmplitudeCal = json_data.get('zLeftStepAmplitudeCal')
    # zLeftStepAmplitudeCal(歩行指標) sa_zlc：歩行振動Z補正有（cm,左足）
    # 0.00-20.00
    zLeftStepAmplitudeCal = json_data.get('zLeftStepAmplitudeCal')

    # maxRightStepAcceleration(歩行指標) st_r：最大着地強度平均 (G, 右足)
    # 0.00-8.00
    maxRightStepAcceleration = json_data.get('maxRightStepAcceleration')
    # maxLeftStepAcceleration(歩行指標) st_l：最大着地強度平均 (G, 左足)
    # 0.00-8.00
    maxLeftStepAcceleration = json_data.get('maxLeftStepAcceleration')

    # sleepScoreStandard(静止指標)sc_slp_std：低覚醒スコア(通常時)
    # まばたき強さ・速度と一部まばたき間隔から「目がトロンとなっている状態」を指標化したもの
    # 有効時: 0(覚醒高い)-100(眠い)、無効: -1
    sleepScoreStandard = json_data.get('sleepScoreStandard')
    # sleepScore(静止指標)sc_slp：低覚醒スコア(運転時)
    # 運転時の姿勢(まっすぐ前を向いている状態)でクレンジングし、精度を高めたもの
    # 有効時: 0(覚醒高い)-100(眠い)、無効: -1
    sleepScore = json_data.get('sleepScore')
    # focusScore(静止指標)sc_fcs：没入スコア
    # まばたき間隔を利用し「ある一つのタスクへの注意が続いている状態」を指標化したもの
    # 有効時: 0(没入度が低い)-100(没入度が高い)、無効: -1
    focusScore = json_data.get('focusScore')
    # tensionScore(静止指標)sc_tsn：テンションスコア
    # まばたき強さを利用し「目が見開いている状態」を指標化したもの
    # 有効時: 0(緊張が弱い)-100(緊張が強い)、無効: -1
    tensionScore = json_data.get('tensionScore')
    # calmScore(静止指標)sc_clm：安定スコア
    # まばたき強さを利用し「外部・内部刺激を受けずに安定している状態」を指標化したもの
    # 有効時: 0(落ち着いていない)-100(落ち着いている)、無効: -1
    calmScore = json_data.get('calmScore')

    # distance distance：サブアプリ動作時 前回区間との移動距離(m)
    # 0-5000
    distance = json_data.get('distance')
    # latitude lat：サブアプリ動作時 緯度
    # -180 - 180
    latitude = json_data.get('latitude')
    # longitude lng：サブアプリ動作時 経度
    # -90 - 90
    longitude = json_data.get('longitude')
    # appMeasurementStatus app_measurement_status：サブアプリの動作状況フラグ
    # 0: 非APP測定 2: Run測定中 3: Run一時停止中 8: Drive測定中
    # 12: Drive一時停止中 32: Focus測定中 48: Focus一時停止中
    appMeasurementStatus = json_data.get('appMeasurementStatus')

    # nptMean(静止指標)npt_av：NPT（実効まばたき速度）平均
    # -0.999 - 0.999
    nptMean = json_data.get('nptMean')
    # nptMedian(静止指標)npt_med：NPT（実効まばたき速度）中央値
    # -0.999 - 0.999
    nptMedian = json_data.get('nptMedian')
    # nptSD(静止指標)npt_sd：NPT標準偏差
    # 0-0.999
    nptSD = json_data.get('nptSD')

    # blinkWidthMean(静止指標)bkw_av：まばたき速度平均(mSec)
    # 0-300
    blinkWidthMean = json_data.get('blinkWidthMean')
    # blinkStrengthTotal(静止指標)bkh_sum：まばたき強度合計(uV-equiv)
    # 0-10000.0
    blinkStrengthTotal = json_data.get('blinkStrengthTotal')
    # blinkStrengthMax(静止指標)bkh_max：まばたき強度最大(uV-equiv)
    # 0-1000.0
    blinkStrengthMax = json_data.get('blinkStrengthMax')
    # blinkStrengthSD(静止指標)bkh_sd：まばたき強度標準偏差(uV-equiv)
    # 0.00-1000.0
    blinkStrengthSD = json_data.get('blinkStrengthSD')
    # blinkStrengthMean(静止指標)bkh_av：まばたき強度平均
    # 0-1000.0
    blinkStrengthMean = json_data.get('blinkStrengthMean')

    # blinkIntervalTotal(静止指標)bki_sum：まばたき間隔合計(s)
    # 0-120.0
    blinkIntervalTotal = json_data.get('blinkIntervalTotal')
    # blinkIntervalCount(静止指標)bki_n：まばたき間隔数
    # 0-120
    blinkIntervalCount = json_data.get('blinkIntervalCount')
    # blinkIntervalMean(静止指標)bki_av：まばたき間隔平均
    # 0.00-60.00
    blinkIntervalMean = json_data.get('blinkIntervalMean')

    # blinkCount(静止指標)bk_n：まばたき回数
    # 0-120
    blinkCount = json_data.get('blinkCount')
    # blinkCountRaw(静止指標)rbk_n：まばたき回数生値
    # 0-255
    blinkCountRaw = json_data.get('blinkCountRaw')

    # eyeMoveUpCount(静止指標)re_u：視線移動上回数生値
    # 0-255
    eyeMoveUpCount = json_data.get('eyeMoveUpCount')
    # eyeMoveDownCount(静止指標)re_d：視線移動下回数生値
    # 0-255
    eyeMoveDownCount = json_data.get('eyeMoveDownCount')
    # eyeMoveRightCount(静止指標)re_r：視線移動右回数生値
    # 0-255
    eyeMoveRightCount = json_data.get('eyeMoveRightCount')
    # eyeMoveLeftCount(静止指標)re_l：視線移動左回数生値
    # 0-255
    eyeMoveLeftCount = json_data.get('eyeMoveLeftCount')

    # cummulativeTime cum_time：規格化累積時間(s)
    # 0-4294967296
    cummulativeTime = json_data.get('cummulativeTime')

    # blinkIntervalMeanWA(静止指標)bki_av_wa：まばたき間隔平均 規格化値
    # 0.00-60.00
    blinkIntervalMeanWA = json_data.get('blinkIntervalMeanWA')
    # blinkStrengtnSDWA(静止指標)bkh_sd_wa：まばたき強度標準偏差 規格化値
    # 0.00-1000.0
    blinkStrengtnSDWA = json_data.get('blinkStrengtnSDWA')
    # blinkStrengthMeanWA(静止指標)bkh_av_wa：まばたき強度平均 規格化値
    # 0-1000.0
    blinkStrengthMeanWA = json_data.get('blinkStrengthMeanWA')
    # nptMeanWA(静止指標)npt_av_wa：NPT（実効まばたき速度）平均 規格化値
    # -0.999 - 0.999
    nptMeanWA = json_data.get('nptMeanWA')
    # nptSDWA(静止指標)npt_sd_wa：NPT（実効まばたき速度）標準偏差 規格化値
    # 0-0.999
    nptSDWA = json_data.get('nptSDWA')
    # blinkWidthMeanWA(静止指標)bkw_av_wa：まばたき速度平均 規格化値
    # 0-300
    blinkWidthMeanWA = json_data.get('blinkWidthMeanWA')

    # nptScore(静止指標)sc_npt：覚醒サブ指標 NPTスコア
    # 有効時: 0-100、無効: -1
    nptScore = json_data.get('nptScore')
    # btsScore(静止指標)sc_bts：覚醒サブ指標 BTSスコア
    # 有効時: 0-100、無効: -1
    btsScore = json_data.get('btsScore')
    # lbsScore(静止指標)sc_lbs：覚醒サブ指標 LBSスコア
    # 有効時: 0-100、無効: -1
    lbsScore = json_data.get('lbsScore')

    # legacyZone(静止指標)zone：RTアルゴリズム動作時 zone値
    # 有効時: 0-100、無効: -1
    legacyZone = json_data.get('legacyZone')
    # legacyFocus(静止指標)focus：RTアルゴリズム動作時 focus値
    # 有効時: 0-100、無効: -1
    legacyFocus = json_data.get('legacyFocus')
    # legacyCalm(静止指標)calm：RTアルゴリズム動作時 calm値
    # 有効時: 0-100、無効: -1
    legacyCalm = json_data.get('legacyCalm')
    # legacyPosture(静止指標)posture：RTアルゴリズム動作時 posture値
    # 有効時: 0-100、無効: -1
    legacyPosture = json_data.get('legacyPosture')

    print('date:' + str(date))

    print('stepCount:' + str(stepCount))
    print('stepCadence:' + str(stepCadence))

    print('isStill:' + str(isStill))

    print('betteryLevel:' + str(betteryLevel))

    print('noiseTime:' + str(noiseTime))
    print('isValid:' + str(isValid))

    print('xMean:' + str(xMean))
    print('xSD:' + str(xSD))
    print('yMean:' + str(yMean))
    print('ySD:' + str(ySD))

    print('pitchOnewayCount:' + str(pitchOnewayCount))
    print('pitchRoundCount:' + str(pitchRoundCount))
    print('yawOnewayCount:' + str(yawOnewayCount))
    print('yawRoundCount:' + str(yawRoundCount))

    print('xRightStepAmplitude:' + str(xRightStepAmplitude))
    print('xLeftStepAmplitude:' + str(xLeftStepAmplitude))
    print('yRightStepAmplitude:' + str(yRightStepAmplitude))
    print('yLeftStepAmplitude:' + str(yLeftStepAmplitude))
    print('zRightStepAmplitude:' + str(zRightStepAmplitude))
    print('zLeftStepAmplitude:' + str(zLeftStepAmplitude))
    print('zLeftStepAmplitudeCal:' + str(zLeftStepAmplitudeCal))
    print('zLeftStepAmplitudeCal:' + str(zLeftStepAmplitudeCal))

    print('maxRightStepAcceleration:' + str(maxRightStepAcceleration))
    print('maxLeftStepAcceleration:' + str(maxLeftStepAcceleration))

    print('sleepScoreStandard:' + str(sleepScoreStandard))
    print('sleepScore:' + str(sleepScore))
    print('focusScore:' + str(focusScore))
    print('tensionScore:' + str(tensionScore))
    print('calmScore:' + str(calmScore))

    print('distance:' + str(distance))
    print('latitude:' + str(latitude))
    print('longitude:' + str(longitude))
    print('appMeasurementStatus:' + str(appMeasurementStatus))

    print('nptMean:' + str(nptMean))
    print('nptMedian:' + str(nptMedian))
    print('nptSD:' + str(nptSD))

    print('blinkWidthMean:' + str(blinkWidthMean))
    print('blinkStrengthTotal:' + str(blinkStrengthTotal))
    print('blinkStrengthMax:' + str(blinkStrengthMax))
    print('blinkStrengthSD:' + str(blinkStrengthSD))
    print('blinkStrengthMean:' + str(blinkStrengthMean))

    print('blinkIntervalTotal:' + str(blinkIntervalTotal))
    print('blinkIntervalCount:' + str(blinkIntervalCount))
    print('blinkIntervalMean:' + str(blinkIntervalMean))

    print('blinkCount:' + str(blinkCount))
    print('blinkCountRaw:' + str(blinkCountRaw))

    print('eyeMoveUpCount:' + str(eyeMoveUpCount))
    print('eyeMoveDownCount:' + str(eyeMoveDownCount))
    print('eyeMoveRightCount:' + str(eyeMoveRightCount))
    print('eyeMoveLeftCount:' + str(eyeMoveLeftCount))

    print('cummulativeTime:' + str(cummulativeTime))

    print('blinkIntervalMeanWA:' + str(blinkIntervalMeanWA))
    print('blinkStrengtnSDWA:' + str(blinkStrengtnSDWA))
    print('blinkStrengthMeanWA:' + str(blinkStrengthMeanWA))
    print('nptMeanWA:' + str(nptMeanWA))
    print('nptSDWA:' + str(nptSDWA))
    print('blinkWidthMeanWA:' + str(blinkWidthMeanWA))

    print('nptScore:' + str(nptScore))
    print('btsScore:' + str(btsScore))
    print('lbsScore:' + str(lbsScore))

    print('legacyZone:' + str(legacyZone))
    print('legacyFocus:' + str(legacyFocus))
    print('legacyCalm:' + str(legacyCalm))
    print('legacyPosture:' + str(legacyPosture))


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
