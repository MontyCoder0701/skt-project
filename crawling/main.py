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


# 11번가 크롤링
driver = get_driver()
driver.get("https://www.11st.co.kr/")

wait = WebDriverWait(driver, 5)


def find(wait, css_selector):
    return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))


search = find(wait, "#tSearch > form > fieldset > input")
search.send_keys("후드티\n")

recommend_1 = wait.until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, "#layBodyWrap > div > div > div.l_search_content > div > section:nth-child(3) > ul > li:nth-child(1) > div > div.c_card_info > div.c_prd_name.c_prd_name_row_2")))
print(recommend_1.text)

recommend_2 = wait.until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, "#layBodyWrap > div > div > div.l_search_content > div > section:nth-child(3) > ul > li:nth-child(2) > div > div.c_card_info > div.c_prd_name.c_prd_name_row_2")))
print(recommend_2.text)

recommend_3 = wait.until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, "#layBodyWrap > div > div > div.l_search_content > div > section:nth-child(3) > ul > li:nth-child(3) > div > div.c_card_info > div.c_prd_name.c_prd_name_row_2")))
print(recommend_3.text)

recommend_4 = wait.until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, "#layBodyWrap > div > div > div.l_search_content > div > section:nth-child(3) > ul > li:nth-child(4) > div > div.c_card_info > div.c_prd_name.c_prd_name_row_2")))
print(recommend_4.text)

recommend_5 = wait.until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, "#layBodyWrap > div > div > div.l_search_content > div > section:nth-child(3) > ul > li:nth-child(5) > div > div.c_card_info > div.c_prd_name.c_prd_name_row_2")))
print(recommend_5.text)

driver.close()


# 기상청 크롤링
driver = get_driver()
driver.get(
    "https://www.accuweather.com/ko/kr/boramae-dong/2332264/current-weather/2332264")

wait = WebDriverWait(driver, 5)


def find(wait, css_selector):
    return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))


weather = wait.until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, "body > div.template-root > div.two-column-page-content > div.page-column-1 > div.page-content.content-module > div.current-weather-card.card-module.content-module > div.card-content > div.current-weather > div.current-weather-info > div > div")))
print(weather.text)

driver.close()
