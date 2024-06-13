import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# WebDriverをセットアップ
options = webdriver.ChromeOptions()
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
driver.get('https://rugugu.jp/2048/')

# 少し待ってからゲームを開始
time.sleep(2)

# ゲームの繰り返し動作
try:
    game_board = driver.find_element('tag name', 'body')
    while True:
        game_board.send_keys(Keys.UP)
        time.sleep(0.1)
        game_board.send_keys(Keys.RIGHT)
        time.sleep(0.1)
        game_board.send_keys(Keys.DOWN)
        time.sleep(0.1)
        game_board.send_keys(Keys.LEFT)
        time.sleep(0.1)
except KeyboardInterrupt:
    print("ゲーム終了")
finally:
    driver.quit()
