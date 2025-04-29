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


## 定期実行
### Linuxでの実行
下記のようなbashスクリプトを作成し、crontabに追記
```bash
#!/bin/bash

# 作業ディレクトリに移動
cd (プロジェクトフォルダへの絶対パス)

# ログ出力先
LOGFILE="./log/observe_$(date +'%Y%m%d_%H%M%S').log"

# Docker起動
docker compose up -d

# Selenium が起動するまで待機
for i in {1..30}; do
    if curl -s http://localhost:4444/status | grep -q "ready"; then
        echo "✅ Selenium is ready."
        break
    fi
    echo "⌛ Waiting for Selenium... ($i)"
    sleep 1
done

# メイン処理実行
docker compose exec backend python observe.py >> "$LOGFILE" 2>&1

# コンテナ停止（任意）
docker compose down
```
### Windowsでの実行
下記のようなexec.ps1ファイルを作成し、スケジューラーに登録
```
cd C:(プロジェクトフォルダへの絶対パス)

# コンテナ起動
docker compose up -d

# Seleniumが立ち上がるまで待機（最大30秒）
$timeout = 30
$elapsed = 0
$ready = $false

while (-not $ready -and $elapsed -lt $timeout) {
    try {
        Invoke-WebRequest -Uri "http://localhost:4444/status" -UseBasicParsing | Out-Null
        $ready = $true
    } catch {
        Start-Sleep -Seconds 1
        $elapsed++
    }
}

if ($ready) {
    Write-Output "✅ Selenium is ready. Starting main script..."
    docker compose exec backend python main.py >> log.log
} else {
    Write-Output "❌ Selenium did not start in time."
}

# 終了処理（任意）
docker compose down
```
