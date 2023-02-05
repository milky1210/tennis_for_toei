import time  # スリープを使うために必要
import json
from selenium import webdriver  # Webブラウザを自動操作する（python -m pip install selenium)
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options


class Observer:
    def __init__(self, visible=True):
        json_open = open("pw_id.json", "r")
        json_load = json.load(json_open)
        self.ID = json_load["ID"]
        self.PW = json_load["PW"]
        if visible:
            self.driver = webdriver.Chrome()
        else:
            options = Options()
            options.add_argument("--headless")
            self.driver = webdriver.Chrome(options=options)

    def sclick(self, xpath, shift=False):

        time.sleep(0.2)
        if shift:
            element = self.driver.find_element(By.XPATH, xpath)
            actions = ActionChains(self.driver)  # ActionChainを作成
            actions.key_down(Keys.SHIFT)
            actions.click(element)
            actions.perform()
        else:
            self.driver.find_element(By.XPATH, xpath).click()

    def sclicks(self, xpaths, shift=False):
        for xpath in xpaths:
            self.sclick(xpath, shift)

    def observe(self, month=0, date_time=[[5, 6, 5]]):
        # month: 0->今月,1->来月
        # date: 取りたい日付のリスト
        # time: 取りたい時
        self.driver.get(
            "https://yoyaku.sports.metro.tokyo.lg.jp/user/view/user/homeIndex.html"
        )
        time.sleep(2)
        self.sclick(
            "/html/body/div/form[2]/table/tbody/tr/td[1]/table/tbody/tr[1]/td/div/a/img"
        )
        time.sleep(0.2)
        self.driver.find_element(
            By.XPATH,
            "/html/body/div/form[2]/table/tbody/tr/td/div/table/tbody/tr[2]/td/div/table/tbody/tr[1]/td[2]/div/input",
        ).send_keys(self.ID)
        time.sleep(0.2)
        self.driver.find_element(
            By.XPATH,
            "/html/body/div/form[2]/table/tbody/tr/td/div/table/tbody/tr[2]/td/div/table/tbody/tr[2]/td[2]/div/input",
        ).send_keys(self.PW)
        time.sleep(2)
        self.sclicks(
            [
                "/html/body/div/form[2]/table/tbody/tr/td/div/table/tbody/tr[2]/td/div/table/tbody/tr[3]/td[2]/div/input[1]",
                "/html/body/div/table/tbody/tr/td[2]/form/div/table[3]/tbody/tr[2]/td/div/table[1]/tbody/tr[2]/td[1]/div/a/img",
                "/html/body/div/form[2]/table/tbody/tr/td[2]/div/table/tbody/tr[2]/td/div/div/table/tbody[2]/tr[24]/td[4]/div/input",
            ]
        )
        # ボタン連打
        got_list = []
        for dt in date_time:
            xpath = "/html/body/div/form[2]/table/tbody/tr/td[1]/table[1]/tbody/tr[2]/td/div/span/table[2]/tbody/tr[{}]/td[{}]/div/a".format(
                dt[0], dt[1]
            )
            if (
                len(self.driver.find_elements(By.XPATH, xpath)) > 0
            ):  # find_elementsの複数形に注意
                self.sclick(xpath)
            xpath = "/html/body/div/form[2]/table/tbody/tr/td[2]/div/table[1]/tbody/tr[2]/td/div/div/table[2]/tbody/tr[4]/td[{}]/div/div/img".format(
                dt[2]
            )
            if (
                len(self.driver.find_elements(By.XPATH, xpath)) > 0
            ):  # find_elementsの複数形に注意
                self.sclick(xpath)
            self.sclick(
                "/html/body/div/form[2]/table/tbody/tr/td[2]/div/table[2]/tbody/tr[2]/td/div/table/tbody/tr/td/input"
            )
            if False:  # 次を実行で確定
                self.sclick(
                    "/html/body/div/form[2]/table/tbody/tr/td[2]/div/table[2]/tbody/tr[2]/td/div/table/tbody/tr/td[1]/input"
                )
        time.sleep(100)
        self.driver.quit()
        return []


if __name__ == "__main__":
    # observerのテスト用スクリプト
    observer = Observer(visible=True)
    observer.observe(month=0, date_time=[[5, 6, 5]])
