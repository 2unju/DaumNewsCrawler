# DaumNewsCrawler

[다음 뉴스](https://news.daum.net/)에서 하루 전 일자부터 [max-num](https://github.com/2unju/DaumNewsCrawler/blob/master/daum-news-crawler/arguments.py)개의 뉴스기사를 크롤링합니다. 크롤링 결과는 하위 폴더에 아래와 같은 형태로 저장됩니다. 한 폴더당 1,500개의 기사가 저장됩니다.
```text
DaumNewsCrawler/
       ├ arguments.py
       ├ ...
       └ news/
          ├ (category name)/
          │       ├  0001/
          │       │    └ news.txt
          │       └ ...
          └ ...
```

## Preprocessing
특수문자, 이메일, 전화번호, url, 언론사 및 기자명 등을 제거합니다. 자세한 사항은 [코드](https://github.com/2unju/DaumNewsCrawler/blob/master/daum-news-crawler/cleaner.py)를 참고해주시기 바랍니다.

## Setting
```shell
pip install requirements.txt
```

## Usage
```shell
Usage: python run.py
Options:
      --multiprocessing Use multiprocessing, default=True
      --num-process     Number of processes when using multiprocessing, default=5
      --logger          Use logger(when go to previous date, go to next page, save, ...), default=True
      --max-num         Number of articles to crawl, default=200,000
      --category        Categories to crawl, choices=["all", "politics", "economic", "culture", "digital", "society"], default="all"
```

## Results
![image](https://user-images.githubusercontent.com/77797199/171593097-56dce7ac-5469-465d-92a8-de743d913a9f.png)
수집된 뉴스는 txt 확장자로 저장됩니다.
