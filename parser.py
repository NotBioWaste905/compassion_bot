from matplotlib.pyplot import cla
import requests
from bs4 import BeautifulSoup as bs
import json
import re

urls = ["https://psiholog.ru/vopros/28262", "https://psiholog.ru/vopros/28258", "https://psiholog.ru/vopros/28275", "https://psiholog.ru/vopros/28252", "https://psiholog.ru/vopros/28211", "https://psiholog.ru/vopros/28198", "https://psiholog.ru/vopros/28162"]
posts = {}

for url in urls:
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

with open('dictionaries/q_a.json', 'w', encoding="utf-8") as f:
    f.write(json.dumps(posts, ensure_ascii=False, indent=2))
