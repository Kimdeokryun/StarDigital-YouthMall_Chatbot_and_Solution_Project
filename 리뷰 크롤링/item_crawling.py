import requests
from bs4 import BeautifulSoup
from naver_review_crawling import naver_get_review
from idus_review_crawling import idus_get_review, search_idus_items
from coupang_review_crawling import coupang_get_review, search_coupang_items

import pandas as pd
from datetime import datetime


def crawl_items_main(url):
    items = []
    current_date = datetime.now().strftime("%Y-%m-%d_%H-%M")
    if url.find("smartstore") != -1:
        items = naverstore(items, url)
        output_file = f"naver_itemreview_{current_date}.xlsx"
    elif url.find("idus") != -1:
        items = idusstore(items, url)
        output_file = f"idus_itemreview_{current_date}.xlsx"
    elif url.find("coupang") != -1:
        items = coupang(items, url)
        output_file = f"coupang_itemreview_{current_date}.xlsx"

    df = pd.DataFrame(items)
    df = df.drop_duplicates()
    print(df)

    df.to_excel(output_file, index=False, engine='openpyxl')


def naverstore(items, url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # 원하는 태그의 id 값을 이용하여 해당 요소를 찾습니다.
    target_element = soup.find(id="pc-wholeProductWidget")

    # 찾은 요소에서 모든 <a> 태그를 찾아서 href 속성을 추출합니다.
    if target_element:
        a_tags = target_element.find_all("a")
        for a_tag in a_tags:
            origin_url = "https://smartstore.naver.com"
            href = a_tag.get("href")
            item_url = origin_url + href
            print(item_url)

            item_name, review_list = naver_get_review(item_url)

            if len(review_list) != 0:
                for review in review_list:
                    item = {
                        "item_name": item_name,
                        "item_url": item_url,
                        "item_review": review
                    }
                    items.append(item)

    else:
        print("해당 요소를 찾을 수 없습니다.")

    return items


def idusstore(items, url):
    item_urls = search_idus_items(url)
    if len(item_urls) != 0:
        for item_url in item_urls:
            print(item_url)
            item_name, review_list = idus_get_review(item_url)
            if len(review_list) != 0:
                for review in review_list:
                    item = {
                        "item_name": item_name,
                        "item_url": item_url,
                        "item_review": review
                    }
                    items.append(item)
    else:
        print("해당 요소를 찾을 수 없습니다.")

    return items


def coupang(items, url):
    item_urls = search_coupang_items(url)
    if len(item_urls) != 0:
        for item_url in item_urls:
            print(item_url)
            item_name, review_list = coupang_get_review(item_url)
            if len(review_list) != 0:
                for review in review_list:
                    item = {
                        "item_name": item_name,
                        "item_url": item_url,
                        "item_review": review
                    }
                    items.append(item)
    else:
        print("해당 요소를 찾을 수 없습니다.")


    return items




# crawl_items_main("")