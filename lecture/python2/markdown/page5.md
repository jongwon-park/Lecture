## 크롤링

- 데이터 가져오기 : reuests 모듈 이용
- 데이터 정제 : BeautifulSoup 이용

```bash
$ conda install beautifulsoup4
```

```python
### naver_movie.py

import requests

URL = 'https://movie.naver.com/movie/sdb/rank/rmovie.naver'
res = requests.get(URL)
print(res.content)
```
