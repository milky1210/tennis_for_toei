from observe import Observer


def main():
    # 処理開始
    with open("yoyaku_list.txt", "r") as f:
        lines = f.readlines()
    print(f"⚡ 処理開始. 合計{len(lines)}件の予約を処理します。")
    for line in lines:
        park_id, date, hour = line.strip().split(",")
        observer = Observer(visible=True)
        observer.observe(park_id=park_id.strip(), date = date.strip(), hour = hour.strip())


if __name__ == "__main__":
    main()