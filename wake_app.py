import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wake_streamlit_app():
    # AMU-NETデモアプリのURL
    url = "https://amunet-demo-app-kpwa2zadgv8ktbac94e2un.streamlit.app/"
    print(f"URLにアクセス中: {url}")

    # 自動ブラウザ（ヘッドレス）の設定
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    try:
        # ブラウザ起動
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)
        time.sleep(5)  # 読み込み待機

        # 「Yes, get this app back up!」ボタンを探す
        try:
            wait = WebDriverWait(driver, 10)
            button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Yes, get this app back up!')]")))
            
            print("スリープ画面を検知。ボタンをクリックして起こします...")
            button.click()
            time.sleep(10)  # 起き上がるのを待機
            print("デモアプリの起動に成功しました！")
            
        except Exception:
            print("アプリはすでに起きています。ボタンを押す必要はありません。")

    except Exception as e:
        print(f"エラーが発生しました: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    wake_streamlit_app()
