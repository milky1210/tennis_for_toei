import time
import json
import uuid
import os
import tempfile
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select

class Observer:
    def __init__(self):
        with open("pw_id.json", "r") as f:
            creds = json.load(f)
        self.ID = creds["ID"]
        self.PW = creds["PW"]

        options = Options()
        options.binary_location = "/usr/bin/chromium"
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920x1080")

        self.driver = webdriver.Remote(
            command_executor=os.getenv("SELENIUM_URL", "http://selenium:4444/wd/hub"),
            options=options
        )

    def sclick(self, xpath, shift=False):
        time.sleep(0.2)
        element = self.driver.find_element(By.XPATH, xpath)
        actions = ActionChains(self.driver)
        if shift:
            actions.key_down(Keys.SHIFT)
        actions.click(element)
        actions.perform()

    def sclicks(self, xpaths, shift=False):
        for xpath in xpaths:
            self.sclick(xpath, shift)
        
    def observe(self, park_id = '1060', date='20250529', hour = '10'):

        # ページアクセス
        self.driver.get("https://kouen.sports.metro.tokyo.lg.jp/web/index.jsp")
        time.sleep(0.2)
        try:
            self.sclick('//*[@id="btn-login"]')
            ## IDとPWを入力
            time.sleep(0.2)
            self.driver.find_element(By.XPATH, '//*[@id="userId"]').send_keys(self.ID)
            time.sleep(0.2)
            self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(self.PW)
            ## ログインボタンを押す
            self.sclick('//*[@id="btn-go"]')
            ## 日付を選択
            self.driver.find_element(By.XPATH, '//*[@id="daystart-home"]').send_keys(date[4:] + date[:4])
            ## 種目を選択
            sports_dropdown = Select(self.driver.find_element(By.XPATH, '//*[@id="purpose-home"]'))
            sports_dropdown.select_by_value('1000_1030')
            # 公園リストが更新されるのを待つ
            time.sleep(1)
            ## 公園を選択
            park_dropdown = Select(self.driver.find_element(By.XPATH, '//*[@id="bname-home"]'))
            park_dropdown.select_by_value(park_id)
            # 検索
            self.sclick('//*[@id="btn-go"]')
            time.sleep(15)
            # 時間を選択
            self.sclick(f'//*[@id="{date}_{hour}"]/div')
            # 予約ボタンをクリック
            self.sclick('//*[@id="btn-go"]')
            time.sleep(1)
            self.driver.find_element(By.XPATH, '//*[@id="peoples0"]').send_keys('4')
            # 確定ボタンをクリック
            self.sclick('//*[@id="btn-go"]')
            # ポップアップに対してOKをクリック
            self.driver.switch_to.alert.accept()

            
        except Exception as e:
            print(f"Error: {e}")
            self.driver.quit()
            return
        print("Access successful!")

        # 終了処理
        self.driver.quit()

if __name__ == "__main__":
    observer = Observer()
    observer.observe(park_id = '1060', date = '20250531', hour = '10')
