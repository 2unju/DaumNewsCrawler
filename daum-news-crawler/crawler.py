import os
import datetime
import requests

from logger import make_logger
from arguments import get_args
from utils import sleep_page, get_header
from crawler_utils import is_page, save_news, get_news


MAX_NUM = 200000


def news(category):
    args = get_args()
    _url = "https://news.daum.net/breakingnews/"

    if args.logger:
        logger = make_logger()
        logger.info("get from news")

    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, 'news')
    if not os.path.exists(path):
        os.makedirs(path)

    prev = 1

    td = (datetime.datetime.now() - datetime.timedelta(days=prev)).strftime("%Y%m%d")
    dir_cnt = 1

    if not os.path.exists(os.path.join(path, category)):
        os.makedirs(os.path.join(path, category))

    cnt = 0
    tot = 0

    url = _url + category + "?regDate=" + td
    req = requests.get(url, headers=get_header())

    contents = list()

    next_page = True
    page = 1
    while tot < MAX_NUM:
        while next_page and tot < MAX_NUM:
            cnt += get_news(req, contents)

            page += 1
            if args.logger:
                logger.info("{} | {} | next page | {}".format(category, td, page))

            url = _url + category + "?page={}&regDate={}".format(page, td)
            req = requests.get(url, headers=get_header())
            next_page = is_page(req, page)

            if cnt > 1500:
                tot += cnt

                if args.logger:
                    logger.info("{} | tot {}".format(category, tot))

                save_news(contents, path, category, logger, '%04d' % (dir_cnt))
                dir_cnt += 1
                cnt = 0
                contents = list()
                sleep_page()

        if tot < MAX_NUM and not next_page:
            if args.logger:
                logger.info("{} | prev date".format(category))

            prev += 1
            page = 1
            td = (datetime.datetime.now() - datetime.timedelta(days=prev)).strftime("%Y%m%d")

            url = _url + category + "?page={}&regDate={}".format(page, td)
            req = requests.get(url, headers=get_header())
            next_page = is_page(req, page)
        else:
            if not args.logger:
                logger = None
            save_news(contents, path, category, logger, '%04d' % (dir_cnt))
            break
