from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs
import time
import re


def search_idus_items(url):
    url_list = []
    driver_setting(url)
    time.sleep(2)
    items = driver.find_element(By.XPATH, '//*[@id="content"]/div/section[2]/div[2]/div/div[3]/div')
    soup = bs(items.get_attribute('innerHTML'), 'html.parser')

    # <a> 태그의 href 추출
    for a_tag in soup.find_all('a'):
        origin_url = "https://www.idus.com"
        href = a_tag.get('href')
        print(origin_url+href)
        url_list.append(origin_url+href)

    return url_list


def driver_setting(url):
    global driver
    # Chrome 웹 드라이버 경로 설정
    chrome_driver_path = "chromedriver.exe"
    service = Service(executable_path=chrome_driver_path)
    # 웹 드라이버 설정
    chrome_options = Options()
    chrome_options.add_argument('window-size=1920,1080')
    # chrome_options.add_argument('headless')
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
        try:
            some_tag = driver.find_element(By.ID, 'prd-review')
            action = ActionChains(driver)
            action.move_to_element(some_tag).perform()
            time.sleep(1)
            try:
                element = driver.find_element(By.XPATH, '//*[@id="prd-review"]/div/h3').text
                match = re.search(r'\((\d+)\)', element)
                if match:
                    element = match.group(1)
                    print(element)
                break
            except:
                count += 1
                continue
        except:
            break
    return element


def idus_get_review(item_url):
    driver_setting(item_url)

    item_name = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/aside/div/div/h2').text
    element = doScrollDown()

    review_list = []

    if element == "":
        return item_name, review_list

    stop = int(element) // 10

    for pagenum in range(1, stop + 2):
        try:
            review_list = review_parsing(item_url, pagenum, review_list)
        except:
            break

    print(item_name)
    print(review_list)

    return item_name, review_list


def review_parsing(item_url, pagenum, review_list):
    print(item_url + "?review_page=" + str(pagenum))
    driver.get(item_url + "?review_page=" + str(pagenum))
    driver.implicitly_wait(2)

    try:

        some_tag = driver.find_element(By.CLASS_NAME, 'review-contents')
        action = ActionChains(driver)
        action.move_to_element(some_tag).perform()
        html = driver.page_source
        soup = bs(html, "html.parser")

        reviews = soup.find_all('div', class_="review-contents")
        for review in reviews:
            try:
                review = re.sub('[^#0-9a-zA-Zㄱ | 가-힇 ]', "", review.text)
                if review.startswith("판매자"):
                    continue
                review_list.append(review)
            except:
                break
    except:
        pass

    return review_list