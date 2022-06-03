import re
import os
import requests
import pandas as pd
from bs4 import BeautifulSoup

from utils import get_header, sleep_page
from cleaner import clean_text

EMAILP = re.compile(".*?@.*?\..*?") # aa@bb.cc
SPECIAL = re.compile('[#\?^@*\"※▶■◆▲●Δ▷◇☞~ㆍ!』‘|`\'…》\”\“\’]')


def is_page(req, _p):
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    try:
        page = re.sub(r'[^0-9]', '', soup.find('em', {"class": "num_page"}).text)
    except:
        return False

    # if soup.find('em', {"class": "num_page"}):
    if int(page) == _p:
        return True
    return False


def isnt_news(text):
    if '[인사]' in text or '[부고]' in text or '[라운지]' in text or '[오늘의 날씨]' in text:
        return True
    return False


def is_video(soup):
    if soup.find('div', {"class": "video_frm"}):
        return True
    return False


def save_news(contents, path, p, logger, dirname):
    if logger:
        logger.info("{} | save".format(p))

    if not os.path.exists(os.path.join(path, p, dirname)):
        os.makedirs(os.path.join(path, p, dirname))

    df = pd.DataFrame(contents, columns=['news'])
    df = df.drop_duplicates(['news'], ignore_index=True)
    cont = df.values.tolist()

    with open(os.path.join(path, p, dirname, 'news.txt'), 'w', encoding='utf-8', newline='') as f:
        for line in cont:
            f.write("%s\n" % line[0])


def get_news(req, contents):
    cnt = 0

    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    hrefs = soup.find_all('a', {"class": "link_thumb"})

    for href in hrefs:
        try:
            _req = requests.get(href.get('href'), headers=get_header())
        except:
            sleep_page(2)
            _req = requests.get(href.get('href'), headers=get_header())
        cont = get_content_news_req(_req, href)

        if not cont or len(cont.split(' ')) < 35:
            continue
        else:
            contents.append(cont.strip())
            cnt += 1

    return cnt


def get_content_news_req(req, href):
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    try:
        tit = soup.find('h3', {"class": "tit_view"}).text
    except:
        print(href)
        return None
    if isnt_news(tit) or is_video(soup):
        return None

    if soup.find_all(['div'], attrs={'dmcf-ptype': 'general'}):
        conts = soup.find_all(['div'], attrs={'dmcf-ptype': 'general'})
    else:
        conts = soup.find_all(['p'], attrs={'dmcf-ptype': 'general'})

    content = list()
    for text in conts:
        if not text.contents:
            continue

        if text.findChildren("strong") != []:
            continue

        try:
            text = clean_text(text.contents[0])
        except: # text = </br>
            continue

        if 'copyright' in text.lower():
            continue

        # if len(text.split(' ')) < 10:
        if SPECIAL.match(text) or len(text.split(' ')) < 5:
            continue
        elif EMAILP.search(text) is not None:
            continue
        else:
            if len(text.split(' ')) < 5:
                continue
            content.append(text)

    return ' '.join(content)
