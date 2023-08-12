from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs
import time
import re

def search_coupang_items(url):
    url_list = []
    driver_setting(url)
    time.sleep(2)
    items = driver.find_element(By.XPATH, '//*[@id="product-list"]')
    soup = bs(items.get_attribute('innerHTML'), 'html.parser')

    # <a> 태그의 href 추출
    for a_tag in soup.find_all('a'):
        href = a_tag.get('href')
        print(href)
        url_list.append(href)

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
            some_tag = driver.find_element(By.ID, 'btfTab')
            action = ActionChains(driver)
            action.move_to_element(some_tag).perform()
            time.sleep(1)
            try:
                element = driver.find_element(By.XPATH, '//*[@id="btfTab"]/ul[2]/li[3]/div/div[4]/section[1]/div[1]/div[2]').text
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


def coupang_get_review(item_url):
    driver_setting(item_url)

    item_name = driver.find_element(By.XPATH, '//*[@id="contents"]/div/div[1]/div[3]/div[3]/h2').text
    element = doScrollDown()
    review_list = []

    if element == "":
        print("review 없음")
        return item_name, review_list

    count = 0
    stop = int(element) // 5

    btn_list = ["button:nth-child(3)", "button:nth-child(4)", "button:nth-child(5)", "button:nth-child(6)", "button:nth-child(7)",
                "button:nth-child(8)", "button:nth-child(9)", "button:nth-child(10)", "button:nth-child(11)",
                "button.sdp-review__article__page__next.js_reviewArticlePageNextBtn"]

    while count <= stop:
        for pagenum in btn_list:
            try:
                driver.implicitly_wait(2)
                html = driver.page_source
                soup = bs(html, "html.parser")
                reviews = soup.find_all('div', class_="sdp-review__article__list__review__content js_reviewArticleContent")
                for review in reviews:
                    try:
                        review = re.sub('[^#0-9a-zA-Zㄱ | 가-힇 ]', "", review.text)
                        if review.startswith("판매자"):
                            continue
                        print(review)
                        review_list.append(review)
                    except:
                        break
                driver.find_element(By.CSS_SELECTOR,
                                    '#btfTab > ul.tab-contents > li.product-review.tab-contents__content > div > '
                                    'div.sdp-review__article.js_reviewArticleContainer > section.js_reviewArticleListContainer > '
                                    'div.sdp-review__article__page.js_reviewArticlePagingContainer > ' + str(
                                        pagenum)).click()
            except:
                break
        count += 1

    print(item_name)
    print(review_list)

    return item_name, review_list