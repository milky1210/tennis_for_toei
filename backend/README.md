# tennis_for_toei
都営コート用のテニスコート監視・予約コード
## 環境整備

Dockerによる管理である
```bash
docker compose up -d --build
```
にてコンテナを起動する

### Docker環境の説明
selenium自体のコンテナとpythonでスクレイピングするためのbackendコンテナ


### 開発手法
backendのコンテナ上でコード編集を行う。
ブラウザの動作は下記の方法でGUIを可視化できる

http://localhost:7900 をブラウザで開く

パスワード：secret を入力

実行中の自動操作をリアルタイムで確認

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
