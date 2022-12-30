from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import requests as req
from bs4 import BeautifulSoup as BS
import time


def get_driver():
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("window-size=10000,10000")
options.add_argument("lang=en-GB")
options.add_argument('--disable-gpu')
options.add_argument("no-sandbox")
options.add_argument('--headless')

# 11번가 크롤링
driver = get_driver()
driver.get("https://www.11st.co.kr/")

wait = WebDriverWait(driver, 5)


def find(wait, css_selector):
    return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))


list_a_m = ["남성 브이넥 니트", "남성 라운드넥 니트", "남성 일자핏 정장", "남성 일자핏 청바지"]
list_a_f = ["여성 브이넥 니트", "여성 라운드넥 가디건", "여성 일자 정장", "여성 일자 바지"]


list_b_m = ["남성 셔츠", "남성 긴팔 니트", "남성 세미와이드", "남성 테이퍼드"]
list_b_f = ["오프숄더 상의", "퍼프소매 상의", "레이스 상의", "셔링 상의",
            "A라인 하의", "하이웨스트 하의", "세미와이드 하의", "테이퍼드핏 하의"]

list_c = ["오버핏 상의", "린넨 상의", "셔츠 상의", "자켓 상의",
          "와이드핏 하의", "루즈핏 하의", "핀턱 하의", "조거팬츠 하의"]

search = find(wait, "#tSearch > form > fieldset > input")
search.send_keys(str(list_b_m[1])+"\n")

# 제품명 출력
# for i in range(1, 6):
#     try:
#         i = wait.until(EC.presence_of_element_located(
#             (By.CSS_SELECTOR, "#layBodyWrap > div > div > div.l_search_content > div > section:nth-child(3) > ul > li:nth-child("+str(i)+") > div > div.c_card_info > div.c_prd_name.c_prd_name_row_2")))
#     except:
#         i = wait.until(EC.presence_of_element_located(
#             (By.CSS_SELECTOR, "#layBodyWrap > div > div > div.l_search_content > div > section:nth-child(2) > ul > li:nth-child("+str(i)+") > div > div.c_card_info > div.c_prd_name.c_prd_name_row_2")))
#     print(i.text)

# 제품 이미지 저장
for i in range(1, 6):
    with open("crawling/image/b/남자/" + str(list_b_m[1]) + "/" + str(list_b_m[1]) + str(i)+".png", 'wb') as file:
        l = driver.find_element(
            "xpath", "//*[@id='layBodyWrap']/div/div/div[3]/div/section[1]/ul/li[" + str(i) + "]/div/div[1]/a/img")
        file.write(l.screenshot_as_png)

# 제품 구매링크 출력
# for i in range(1, 6):
#     try:
#         print(driver.find_element(By.CSS_SELECTOR,
#                                   "#layBodyWrap > div > div > div.l_search_content > div > section:nth-child(3) > ul > li:nth-child(" + str(i) + ") > div > div.c_card_info > div.c_prd_name.c_prd_name_row_2 > a").get_attribute('href'))
#     except:
#         print(driver.find_element(By.CSS_SELECTOR,
#                                   "#layBodyWrap > div > div > div.l_search_content > div > section:nth-child(2) > ul > li:nth-child(" + str(
#                                       i) + ") > div > div.c_card_info > div.c_prd_name.c_prd_name_row_2 > a").get_attribute('href'))

driver.close()

# 기온 크롤링
# driver = get_driver()
# driver.get(
#     "https://www.google.com/search?q=%EB%B3%B4%EB%9D%BC%EB%A7%A4+%EB%82%A0%EC%94%A8&ei=qVWqY-eoD83r-Aab_oCADQ&ved=0ahUKEwinodfM3Zj8AhXNNd4KHRs_ANAQ4dUDCA8&uact=5&oq=%EB%B3%B4%EB%9D%BC%EB%A7%A4+%EB%82%A0%EC%94%A8&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIKCAAQgAQQRhCAAjoKCAAQRxDWBBCwAzoRCC4QgwEQrwEQxwEQsQMQgAQ6BQgAEIAEOgsILhCABBDHARCvAToLCC4QrwEQxwEQgAQ6BAgAEAM6BwgAEB4Q8QQ6BAgAEB46BggAEAgQHkoECEEYAEoECEYYAFD-AliYD2CxEGgDcAF4AIABkwGIAacKkgEEMC4xMJgBAKABAcgBCsABAQ&sclient=gws-wiz-serp")

# wait = WebDriverWait(driver, 5)


# def find(wait, css_selector):
#     return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))


# weather = wait.until(EC.presence_of_element_located(
#     (By.CSS_SELECTOR, "#wob_tm")))
# print(weather.text + "°C")

# # 기온 아이콘 저장
# with open("crawling/weather/icon.png", 'wb') as file:
#     l = driver.find_element(
#         "xpath", "//*[@id='wob_tci']")
#     file.write(l.screenshot_as_png)

# driver.close()
