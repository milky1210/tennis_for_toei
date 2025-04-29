import json, config  # 標準のjsonモジュールとconfig.pyの読み込み
from requests_oauthlib import OAuth1Session  # OAuthのライブラリの読み込み


def tweet_img(filename, txt):
    CK = config.CONSUMER_KEY
    CS = config.CONSUMER_SECRET
    AT = config.ACCESS_TOKEN
    ATS = config.ACCESS_TOKEN_SECRET
    url_media = "https://upload.twitter.com/1.1/media/upload.json"
    url_text = "https://api.twitter.com/1.1/statuses/update.json"
    twitter = OAuth1Session(CK, CS, AT, ATS)  # 認証処理
    files = {"media": open(filename, "rb")}
    req_media = twitter.post(url_media, files=files)

    # レスポンスを確認
    if req_media.status_code != 200:
        print("画像アップデート失敗: %s", req_media.text)
        exit()

    # Media ID を取得
    media_id = json.loads(req_media.text)["media_id"]
    print("Media ID: %d" % media_id)
    # Media ID を付加してテキストを投稿
    params = {"status": txt, "media_ids": [media_id]}
    req_media = twitter.post(url_text, params=params)

    # 再びレスポンスを確認
    if req_media.status_code != 200:
        print("テキストアップデート失敗: %s", req_text.text)
        exit()

    print("OK")


def tweet_txt(txt):
    CK = config.CONSUMER_KEY
    CS = config.CONSUMER_SECRET
    AT = config.ACCESS_TOKEN
    ATS = config.ACCESS_TOKEN_SECRET
    twitter = OAuth1Session(CK, CS, AT, ATS)  # 認証処理
    url = "https://api.twitter.com/1.1/statuses/update.json"
    params = {"status": txt}
    req_media = twitter.post(url, params=params)
    # レスポンスを確認
    if req_media.status_code != 200:
        print("テキストアップデート失敗: %s", req_text.text)
        exit()
