import requests
from bs4 import BeautifulSoup as bs
import json
import re
from tqdm import tqdm

posts = {}

def get_urls(URL, multipage=False):
    urls = []
    if multipage:
        pass
    else:
        page = requests.get(URL)
        soup = bs(page.text, "html.parser")

        links_raw = soup.find_all('div', class_="zag")
        for link in links_raw:
            try:
                link = link.find('a').get("href")
                urls.append("https://psiholog.ru"+link)
            except TypeError:
                print("TypeError")
            finally:
                continue

    return urls

def get_data(URL):
    page = requests.get(url)
    soup = bs(page.text, "html.parser")

    question_raw = soup.find_all('div', class_="text")
    response_raw = soup.find_all('div', class_="otvet")

    question = ''
    response = ''

    for x in question_raw:
        question += x.text + '\n'

    for x in response_raw:
        response += x.text + '\n'

    post = {url: {"question": question, "response": response}}
    posts.update(post)



if __name__ == '__main__':
    for url in tqdm(get_urls("https://psiholog.ru/otvety-psihologov")):
        get_data(url)
    with open('dictionaries/q_a.json', 'w', encoding="utf-8") as f:
        f.write(json.dumps(posts, ensure_ascii=False, indent=2))
