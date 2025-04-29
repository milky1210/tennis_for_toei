from observe import Observer
import datetime

def main():
    # 処理開始
    # 処理時刻をプリント
    print("Processing started at: ", datetime.datetime.now())
    with open("yoyaku_list.txt", "r") as f:
        lines = f.readlines()
    print(f"Starting the reservation process. Total {len(lines)} reservations to process.")
    for line in lines:
        park_id, date, hour = line.strip().split(",")
        observer = Observer()
        observer.observe(park_id=park_id.strip(), date = date.strip(), hour = hour.strip())
    print("All done at: ", datetime.datetime.now())

if __name__ == "__main__":
    main()