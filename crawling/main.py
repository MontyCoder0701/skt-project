from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def get_driver():
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("window-size=1000,1000")
options.add_argument("lang=en-GB")
options.add_argument('--disable-gpu')
options.add_argument("no-sandbox")

driver = get_driver()
driver.get("https://google.com")

wait = WebDriverWait(driver, 5)


def find(wait, css_selector):
    return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))


search = find(wait, "body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input")
search.send_keys("investment\n")

button = find(
    wait, "#hdtb-msb > div:nth-child(1) > div > div:nth-child(2) > a > span")
button.click()

headline_1 = wait.until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, "#rso > div > div > div:nth-child(1) > div > div > a > div > div.iRPxbe > div.mCBkyc.ynAwRc.MBeuO.nDgy9d")))
print(headline_1.text)

headline_2 = wait.until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, "#rso > div > div > div:nth-child(2) > div > div > a > div > div.iRPxbe > div.mCBkyc.ynAwRc.MBeuO.nDgy9d")))
print(headline_2.text)

headline_3 = wait.until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, "#rso > div > div > div:nth-child(3) > div > div > a > div > div.iRPxbe > div.mCBkyc.ynAwRc.MBeuO.nDgy9d")))
print(headline_3.text)

driver.close()
