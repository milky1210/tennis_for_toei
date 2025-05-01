from observe import Observer
import datetime

def main():
    # 処理開始
    # 処理時刻をプリント
    # 日本標準時
    JST = datetime.timezone(datetime.timedelta(hours=9), name='JST')
    dt = datetime.datetime.now(JST)
    print("Processing started at: ", dt.strftime("%Y-%m-%d %H:%M:%S"))
    with open("yoyaku_list.txt", "r") as f:
        lines = f.readlines()
    print(f"Starting the reservation process. Total {len(lines)} reservations to process.")
    for line in lines:
        park_id, date, hour = line.strip().split(",")
        observer = Observer()
        observer.observe(park_id=park_id.strip(), date = date.strip(), hour = hour.strip())
    dt = datetime.datetime.now(JST)
    print("All done at: ", dt.strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == "__main__":
    main()