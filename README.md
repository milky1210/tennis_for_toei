# tennis_for_sinjuku
新宿区用のテニスコート監視・予約コード
## 環境整備

pipなどでパッケージを収集する。

selenium, chrome-driver など

pythonやそのパッケージは利用者の環境次第なので、お好みの方法で必要なライブラリ、ドライバをインストールしてほしい。

## ユーザー情報ファイルに情報書き入れ
sample_pwd_id.jsonファイルに新宿区の団体IDとパスワードを入力し、ファイル名をpwd_id.jsonに変更することで利用できます。


## twitterAPI
必須ではないが結果を呟くためにtwitterAPIと連携している。
利用する場合config.pyを追加し、必要なライセンス情報を足す必要あり。
使わない場合はwithout_twitterのブランチへ

##ビルド方法

python main.py --addSun --addSat --addNight

にて監視用コードを動かし、平日19:00-と土日のコートが空いた時にとる。
詳しくはpython main.py -hから
