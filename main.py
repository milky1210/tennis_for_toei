import argparse
import csv
import time
import tweeter
from observe import Observer
import datetime


def main(args):
    if len(args.timer) > 0:  # もしタイマーがonなら
        set_date = args.timer[0]
        set_hour = 0
        if len(args.timer) > 1:
            set_hour = args.timer[1]
        while 1:
            dt_now = datetime.datetime.now()
            if dt_now.day == set_date and dt_now.hour == set_hour:
                break
            time.sleep(1)
        if len(args.timer) > 2:
            time.sleep(args.timer[2] * 60)

    # 処理開始
    startTime = datetime.datetime.now()
    time_list = []
    if args.addNight:
        for i in range(1, 31, 1):
            if args.month == 0 and i < 3:
                break
            time_list.append([i, 6])
    dt_now = datetime.datetime.now()
    year = dt_now.year
    month = dt_now.month + args.month  # 取る対象の月
    today = dt_now.day
    if month > 12:
        month -= 12
        year += 1
    youbi = datetime.datetime(year, month, 1).weekday()  # 0が月曜日
    if args.addSun:
        begin = 1 + (6 - youbi) % 7
        for i in range(begin, 32, 7):
            for j in range(1, 6):
                if args.month == 0:
                    date = i - today + 1
                    if date < 3 or 30 < date:
                        break
                else:
                    date = i
                time_list.append([date, j])
    if args.addSat:
        begin = 1 + (5 - youbi) % 7
        for i in range(begin, 32, 7):
            for j in range(1, 6):
                if args.month == 0:
                    date = i - today + 1
                    if date < 3 or 30 < date:
                        break
                else:
                    date = i
                time_list.append([date, j])
    if len(args.addDays) > 0:
        for date in args.addDays:
            for j in range(1, 6):
                if args.month == 0:
                    date = date - today + 1
                    if date < 0 or 30 < date:
                        break
                else:
                    date = i
                time_list.append([date, j])

    print("{}件の時間帯の予約を行います。".format(len(time_list)))

    print("observe start")
    observer = Observer(visible=not args.hide)
    result = observer.observe(month=args.month, date_time=time_list)
    endTime = datetime.datetime.now()
    if len(result) > 0:
        txt = "@milky9712, 落合中央公園テニスコート予約成功\n"
        for re in result:
            if args.month == 0:
                date = today + re[0] - 1
            else:
                date = re[0]
            txt = txt + str(date) + "日の," + str(re[1] * 2 + 7) + "時\n"
        txt = txt + "以上の内容になります\n"
        txt = txt + "アクセスログ：{:02}:{:02}:{:02}アクセス開始、{:02}:{:02}:{:02}アクセス完了\n".format(
            startTime.hour,
            startTime.minute,
            startTime.second,
            endTime.hour,
            endTime.minute,
            endTime.second,
        )
        tweeter.tweet_txt(txt)
        print(txt)
    else:
        txt = "@milky9712, 正常に終了(予約は埋めっていました\n"
        txt = txt + "アクセスログ：{:02}:{:02}:{:02}アクセス開始、{:02}:{:02}:{:02}アクセス完了\n".format(
            startTime.hour,
            startTime.minute,
            startTime.second,
            endTime.hour,
            endTime.minute,
            endTime.second,
        )
        if args.errTweet:
            tweeter.tweet_txt(txt)
        print(txt)

    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--month", default=0, type=int, help="今月か来月かを0,1で指定.0:今月、1:来月")
    parser.add_argument("--input", default="", help="日時と時間のarrayファイルを指定.形式はcsv(未実装)")
    parser.add_argument("--addSun", action="store_true", help="日曜日を追加,時間は9-19まで,3日後から")
    parser.add_argument("--addSat", action="store_true", help="土曜日を追加,時間は9-19まで,3日後から")
    parser.add_argument("--addNight", action="store_true", help="夜(19-)の枠のみを表示, 3日後から")
    parser.add_argument(
        "--repeat", default=60, type=int, help="繰り返しのインターバル[min](未実装)"
    )  # min
    parser.add_argument(
        "--addDays",
        default=[],
        nargs="*",
        type=int,
        help="追加したい日付スペース区切りで羅列.(ex: 10 31)",
    )  # 日付のリスト
    parser.add_argument("--hide", action="store_true", help="ドライバを非表示に設定")
    parser.add_argument(
        "--timer",
        default=[],
        nargs="*",
        type=int,
        help="日時指定してそれまで待機, ex: 21 19 で21日の19時にset",
    )
    parser.add_argument("--errTweet", action="store_true", help="エラーでもlogをツイートする")
    args = parser.parse_args()
    main(args)
