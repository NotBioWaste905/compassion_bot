import requests
from bs4 import BeautifulSoup as bs
import json
import re
from tqdm import tqdm

# import util.db_operator as db

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

def get_data(url):
    page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = bs(page.text, "html.parser")

    question_raw = soup.find_all('div', class_="text")
    response_raw = soup.find_all('div', class_="otvet")

    question = ''
    response = ''

    for x in question_raw:
        question += x.text + '\n'

    for x in response_raw:
        response += x.text + '\n'

    # return question, response

    post = {url: {"question": question, "response": response}}
    posts.update(post)
    # print(url)



if __name__ == '__main__':
    # cur, con = db.connect_to_db()
    id = 0
    for page in tqdm(range(0, 28495//2)):
        try:
            get_data(f"https://psiholog.ru/vopros/{page}")
        except:
            print(page, "no data")
            # print(page)
    #         id += 1
    #         q, a = get_data(url)
    #         db.insert_data(cur, con, id, q, a)
    #
    # db.read_data()
    # db.disconnect()
    with open('dictionaries/q_a.json', 'w', encoding="utf-8") as f:
         f.write(json.dumps(posts, ensure_ascii=False, indent=2))
