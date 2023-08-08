from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs
import time
import re

def driver_setting(url):
    global driver
    # Chrome 웹 드라이버 경로 설정
    chrome_driver_path = "chromedriver.exe"
    service = Service(executable_path=chrome_driver_path)
    # 웹 드라이버 설정
    chrome_options = Options()
    chrome_options = Options()
    chrome_options.add_argument('window-size=1920,1080')
    chrome_options.add_argument('headless')
    chrome_options.add_argument("disable-gpu")
    chrome_options.add_argument("disable-infobars")
    chrome_options.add_argument("--disable-extensions")

    # 웹 드라이버 생성
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # 웹 페이지 열기
    driver.get(url)
    driver.implicitly_wait(2)


def doScrollDown():
    count = 0
    element = ""
    while count < 5:
        some_tag = driver.find_element(By.ID, 'REVIEW')
        action = ActionChains(driver)
        action.move_to_element(some_tag).perform()
        time.sleep(1)
        try:
            element = driver.find_element(By.XPATH, '//*[@id="REVIEW"]/div/div[3]/div[1]/div[1]/strong/span').text
            break
        except:
            count += 1
            continue

    return element


def naver_get_review(item_url):
    driver_setting(item_url)

    item_name = driver.find_element(By.XPATH,'//*[@id="content"]/div/div[2]/div[2]/fieldset/div[1]/div[1]/h3').text

    count = 0
    element = doScrollDown()
    stop = int(element) // 11
    btn_list = ["a:nth-child(2)", "a:nth-child(3)", "a:nth-child(4)", "a:nth-child(5)", "a:nth-child(6)",
                "a:nth-child(7)", "a:nth-child(8)", "a:nth-child(9)", "a:nth-child(10)", "a:nth-child(11)",
                "a.fAUKm1ewwo._2Ar8-aEUTq"]

    review_list = []

    if element == "0":
        return item_name, review_list

    while count <= stop:
        for pagenum in btn_list:
            try:
                driver.find_element(By.CSS_SELECTOR,
                                    '#REVIEW > div > div._180GG7_7yx > div.cv6id6JEkg > div > div >' + str(
                                        pagenum) + '').click()
                driver.implicitly_wait(2)
                html = driver.page_source
                soup = bs(html, "html.parser")
                reviews = soup.find_all('div', class_="_19SE1Dnqkf")
                for review in reviews:
                    try:
                        review = re.sub('[^#0-9a-zA-Zㄱ | 가-힇 ]', "", review.text)
                        if review.startswith("판매자"):
                            continue
                        review_list.append(review)
                    except:
                        break
            except:
                break
        count += 1

    return item_name, review_list


