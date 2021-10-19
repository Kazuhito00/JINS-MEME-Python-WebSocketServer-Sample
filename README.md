# JINS-MEME-Python-WebSocketServer-Sample
[JINS MEME(2021年モデル)](https://jinsmeme.com/)のJINS MEME LoggerをPythonのWebSocketサーバーで受信するサンプルです。

# Logging Data
以下のデータに対応しています。<br>
各データの定義は[JINS MEME Platform：データ定義](https://jins-meme.github.io/sdkdoc2/basics/definition.html)を参照ください。
* 20Hzデータ(currentData)<br>約20Hzでデータを取得でき、動きの把握やコントローラーなど<br>精緻なデータの即時取得・分析に適したモードです。<br>このデータはJINS MEMEとスマートフォンがBluetooth接続している時のみ生成されます。
* 15秒間隔データ(logicIndexData)<br>15秒間隔データは生体指標を出力する一番粒度の細かいデータです。<br>このデータはJINS MEMEとスマートフォンがBluetooth接続している時のみ生成されます。
* 60秒間隔データ(summaryData)<br>1分間に1回データを取得できる、長時間の状態変化をモニタリングするのに適したモードです。
* 高速頭部運動データ(fastHeadMotion)<br>0.2〜0.9秒程度の周期で頭を左右、上下に向けた時の最初の方向、回数カウントのイベントです。<br>連続で往復すると回数がカウントアップされ、連続した動作が止まると最終値のみ返されます。<br>回転速度で判定するため、ジャイロセンサーをオンにする必要があります。<br>このデータはJINS MEMEとスマートフォンがBluetooth接続している時のみ生成されます。
* 低速頭部運動データ(slowHeadMotion)<br>頭を真っ直ぐな状態から左右か前後に45°以上傾けて1秒間弱維持した時のイベントです。<br>このデータはJINS MEMEとスマートフォンがBluetooth接続している時のみ生成されます。

# Requirement 
* websocket-server 0.5.6 or later

```bash
pip install websocket-server
```

# Preparation
1. JINS MEME Loggerを起動する<br>[Play Store](https://play.google.com/store/apps/details?id=com.jins_meme.logger4internal)<br>[App Store](https://apps.apple.com/jp/app/jins-meme-logger/id1537937129)
2. JINS MEME Loggerの「接続」タブでJINS MEMEを接続する(要Bluetoothオン)
3. サーバーとなるPCとJINS MEMEを接続したスマホを同じWifiに接続する
4. JINS MEME Loggerの「設定」タブで「ジャイロを取得」をオンにする<br><img src="https://user-images.githubusercontent.com/37477845/137775139-b14de266-f229-4951-8d76-2b6ceb4dcdd4.PNG" width="30%">　<img src="https://user-images.githubusercontent.com/37477845/137775156-c45a094f-ed86-4994-a5e0-a88b5d11d71c.png" width="30%">
5. JINS MEME Loggerの「設定」タブで「WebSocketクライアント」を追加する<br>設定名称：任意の名称を指定<br>Ip Address：PCのIPアドレスを指定<br>Port：8080(必要に応じて任意のポートを指定)<br>Data Tyep：取得したいタイプを指定<br><img src="https://user-images.githubusercontent.com/37477845/137775149-ff23bcfb-7fc0-4965-9717-bae96fa66ab2.PNG" width="30%">　<img src="https://user-images.githubusercontent.com/37477845/137775158-99752c8f-19d9-47d9-9129-aa7301e9fd07.png" width="30%">

# Demo
デモの実行方法は以下です。
```bash
python Sample-currentData.py
    or
python Sample-summaryData.py
    or
python Sample-logicIndexData.py
    or
python Sample-fastHeadMotion.py
    or
python Sample-slowHeadMotion.py
```
* --host<br>
WebSocketServerのPCのIPアドレス ※未指定時は自動でプログラム起動PCのIPを指定<br>
デフォルト：None
* --port<br>
WebSocketServerのPCのポート<br>
デフォルト：8080

# Reference
* [JINS MEME(2021年モデル)](https://jinsmeme.com/)
* [JINS MEME Platform：データ定義](https://jins-meme.github.io/sdkdoc2/basics/definition.html)

# Author
高橋かずひと(https://twitter.com/KzhtTkhs)
 
# License 
JINS-MEME-Python-WebSocketServer-Sample is under [MIT License](LICENSE).
