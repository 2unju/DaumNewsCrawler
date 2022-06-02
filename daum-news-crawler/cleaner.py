import re

CLEANTAG = re.compile('<.*?>')  # HTML tag
CLEANSB = re.compile('\[.*?\]') # [xxx]
CLEANP = re.compile('\(.*?=.*?\)')  # (xxx = xxx)
CLEANP2 = re.compile('.*?=.*?') # xxx = <content>
CLEANP3 = re.compile('(/[가-힣]*.\w?기자)|(/뉴스.*?)')
CLEANYTN = re.compile("YTN 검색해 채널 추가")
CLEANSP = re.compile('[#\?^@*\"※▶■◆▲●Δ▷◇☞~ㆍ!』‘|`\'…》\”\“\’]')
CLEANDT = re.compile(r'\d{2,4}\.\d{1,2}\.\d{1,2}')
CLEANTH = re.compile('\d$')


def clean_reporter(text):
    cleantext = CLEANP.sub('', text)
    cleantext = CLEANP2.sub('', cleantext)
    cleantext = CLEANP3.sub('', cleantext)
    cleantext = CLEANYTN.sub('', cleantext)
    return cleantext


def clean_tag(text):
    cleantext = CLEANTAG.sub('', text)
    cleantext = CLEANSB.sub('', cleantext)
    return cleantext


def clean_others(text):
    cleantext = CLEANTH.sub('', text)
    cleantext = CLEANDT.sub('', cleantext)
    cleantext = re.sub("\n", ' ', cleantext)
    cleantext = re.sub('\s{2,}', ' ', cleantext)
    return cleantext


def clean_text(text):
    cleantext = clean_reporter(text)
    cleantext = clean_tag(cleantext)
    cleantext = clean_others(cleantext)
    return cleantext
