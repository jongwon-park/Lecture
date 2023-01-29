## 네이버 기사 크롤링

```python
import requests
from bs4 import BeautifulSoup
from urllib import parse
import re
import csv 


def get_data(keyword, page):
  start = page * 10 + 1
  keyword_encoded = parse.quote(keyword)
  url = f'https://search.naver.com/search.naver?where=news&sm=tab_pge&query={keyword_encoded}&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=17&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start={start}'
  raw = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'})
  html = BeautifulSoup(raw.text, "html.parser")
  return html

# next button 확인해서, disabled되어 있으면 False리턴, 그 외 True 리턴
def is_next(html):
  next_button = html.select_one("#main_pack > div.api_sc_page_wrap > div > a.btn_next")
  aria_disabled = 'aria-disabled' in next_button.attrs.keys()
  if aria_disabled:
    if next_button['aria-disabled'] == 'true': 
      return False
    else: return True
  else: return True

def parse_data(html):
  articles = html.select("#main_pack > section > div > div.group_news > ul > li")
  data = []
  for article in articles:
    title = article.find('a', 'news_tit').text.strip()
    desc = article.find('div', 'dsc_wrap').text.strip()
    data.append([title, desc])
  return data

def save_csv(data):
  filename = "result.csv"
  f = open(filename, "w", encoding="utf-8-sig", newline="")
  writer = csv.writer(f)
  i = 1
  for item in data:
    writer.writerow([i, item])
    i += 1
  f.close()

def crawling(keyword):
  page = 0
  data = []
  is_continue = True
  while(is_continue):
    html = get_data(keyword, page)
    parsed_data = parse_data(html)
    data = data + parsed_data
    page += 1
    is_continue = is_next(html)
  save_csv(data)

```